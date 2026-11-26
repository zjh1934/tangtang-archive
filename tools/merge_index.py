#!/usr/bin/env python3
"""多对话并发合并器：从远端最新内容出发，追加一轮，幂等、不覆盖历史。

与 lovers/scripts/archive_sync.py 同契约。两边都用这一套合并逻辑，就不会互相抹掉。
用法：
  python3 tools/merge_index.py --self-test
  python3 tools/merge_index.py --apply <repo_root> --manifest <rounds/xxx/manifest.json>
        （--apply 供单写入方 / CI 兜底；并发写入方应直接调下面四个 merge_* 函数，
          在 CAS 循环里基于远端最新正文合并，而不是先写本地再提交）
"""
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = "zjh1934/tangtang-archive"


def merge_readme(text, row_line, keep=10):
    """把本轮行插进 INDEX 标记块，保留最近 keep 轮；本轮已存在就先剔除再追加。"""
    m = re.search(r"(<!-- INDEX:START -->)(.*?)(<!-- INDEX:END -->)", text, re.S)
    if not m:
        return text
    header, rows = [], []
    for l in m.group(2).splitlines():
        if re.match(r"^\|\s*R\d{3}\s*\|", l):
            rows.append(l)
        elif l.strip().startswith("|") and len(header) < 2:
            header.append(l)
    if len(header) < 2:
        header = ["| 轮次 | 主题 | 四图预览 | 穿搭id | 线稿id | 日期 | 现场 |",
                  "|---|---|---|---|---|---|---|"]
    rid = (re.search(r"rounds/([^/]+)/", row_line) or [None, ""])[1]
    rows = [r for r in rows if not (rid and rid in r)] + [row_line]
    return text[:m.start(2)] + "\n" + "\n".join(header + rows[-keep:]) + "\n" + text[m.end(2):]


def merge_archive(text, row_line):
    """台账只追加；本轮目录名已出现就原位置替换（幂等）。"""
    rid = (re.search(r"`([^`]+)`", row_line) or [None, ""])[1]
    out, done = [], False
    for l in text.splitlines():
        if rid and rid in l and re.match(r"^\|\s*R\d{3}\s*\|", l):
            out.append(row_line)
            done = True
        else:
            out.append(l)
    if not done:
        last = max((i for i, l in enumerate(out) if re.match(r"^\|\s*R\d{3}\s*\|", l)), default=-1)
        out.insert(last + 1, row_line)
    return "\n".join(out) + "\n"


def merge_data(text, round_obj):
    """机器数据按目录 id 去重后追加，目录字典序即时间序。"""
    try:
        d = json.loads(text) if text.strip() else {"schema": 1, "repo": REPO, "rounds": []}
    except json.JSONDecodeError:
        d = {"schema": 1, "repo": REPO, "rounds": []}
    d.setdefault("rounds", [])
    d["rounds"] = [r for r in d["rounds"] if r.get("id") != round_obj["id"]] + [round_obj]
    d["rounds"].sort(key=lambda r: r.get("id", ""))
    d["updated_at"] = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n"


def merge_index_html(text, data_obj):
    """画廊内联数据整行替换成合并后的 data。"""
    m = re.search(r"^const DATA = \{.*\};$", text, re.M)
    if not m:
        return text
    line = "const DATA = " + json.dumps(data_obj, ensure_ascii=False) + ";"
    return text[:m.start()] + line + text[m.end():]


def apply(repo_root, manifest_path):
    root = Path(repo_root)
    mf = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    rid, rno = mf["id"], mf["round"]
    base = "rounds/" + rid
    views = [x["file"] for x in mf["images"]]
    row = (f"| R{rno:03d} | {mf['title']} | " + " ".join(
        f'<img width=110 src="{base}/{f}">' for f in views) +
        f" | `{mf['outfit_id']}` | `{mf['images'][0].get('sketch_id','')}` 等 4 张 | {mf['date']} | [本轮]({base}/README.md) |")
    arow = f"| R{rno:03d} | `{rid}` | {mf['title']} | `{mf['outfit_id']}` | {mf['date']} |"
    robj = {
        "round": rno, "id": rid, "date": mf["date"], "title": mf["title"],
        "outfit_id": mf["outfit_id"],
        "sketches": [x.get("sketch_id", "") for x in mf["images"]],
        "base": base,
        "images": [{"file": x["file"], "view": x["view"], "prompt": x["prompt"],
                    "md": f"{base}/{x['prompt']}"} for x in mf["images"]],
        "lines": mf.get("lines", []),
    }
    rd = root / "README.md"
    ar = root / "ARCHIVE.md"
    dj = root / "docs/data.json"
    ih = root / "docs/index.html"
    rd.write_text(merge_readme(rd.read_text(encoding="utf-8"), row), encoding="utf-8")
    ar.write_text(merge_archive(ar.read_text(encoding="utf-8"), arow), encoding="utf-8")
    dnew = merge_data(dj.read_text(encoding="utf-8"), robj)
    dj.write_text(dnew, encoding="utf-8")
    ih.write_text(merge_index_html(ih.read_text(encoding="utf-8"), json.loads(dnew)), encoding="utf-8")
    print("合并完成：", rid, "R%03d" % rno)


def self_test():
    rd = "# T\n\n<!-- INDEX:START -->\n| 轮次 | 主题 |\n|---|---|\n| R001 | 旧 |\n<!-- INDEX:END -->\n尾\n"
    out = merge_readme(rd, "| R002 | 新 | <img src=\"rounds/x/01_front.png\"> |")
    assert "R001" in out and "R002" in out and "尾" in out
    assert merge_readme(out, "| R002 | 新2 | <img src=\"rounds/x/01_front.png\"> |").count("| R002") == 1
    ar = "# A\n\n| 轮次 | 目录 |\n|---|---|\n| R001 | `a` |\n"
    a2 = merge_archive(ar, "| R002 | `x` |")
    assert "R001" in a2 and "R002" in a2
    assert merge_archive(a2, "| R002 | `x` |").count("R002") == 1
    d = merge_data('{"schema":1,"rounds":[{"id":"a","round":1}]}', {"id": "x", "round": 2})
    assert len(json.loads(d)["rounds"]) == 2
    h = "x\nconst DATA = {\"schema\": 1, \"rounds\": []};\ny\n"
    assert '"id": "x"' in merge_index_html(h, json.loads(d))
    print("self-test OK：四条合并函数幂等、不丢历史行")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    elif "--apply" in sys.argv:
        i = sys.argv.index("--apply")
        j = sys.argv.index("--manifest")
        apply(sys.argv[i + 1], sys.argv[j + 1])
    else:
        print(__doc__)
