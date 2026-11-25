#!/usr/bin/env python3
"""扫 rounds/*/manifest.json：校验每轮 4 图 4 md 配对，回写根 README 标记块与 ARCHIVE.md，产出 docs/data.json。"""
import json, re
from pathlib import Path

VIEWS = ["front", "side", "seat", "close"]
root = Path(__file__).resolve().parent.parent
rounds = sorted(p for p in (root / "rounds").iterdir() if p.is_dir() and not p.name.startswith("_"))
data = {"schema": 1, "repo": "zjh1934/tangtang-archive", "rounds": []}
rows = []
for i, d in enumerate(rounds, 1):
    m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    assert len(m["images"]) == 4, f"{d.name}: images 必须 4 条"
    for im in m["images"]:
        assert (d / im["file"]).exists(), f"{d.name}: 缺图 {im['file']}"
        assert (d / im["prompt"]).exists(), f"{d.name}: 缺 md {im['prompt']}"
        assert Path(im["file"]).stem == Path(im["prompt"]).stem, f"{d.name}: 图与 md 不同名"
        assert im["view"] in VIEWS, f"{d.name}: view 不在词表"
        assert (d / im["file"]).stat().st_size < 25 * 1024 * 1024, f"{d.name}: 单图超 25MB"
    b = f"rounds/{d.name}"
    data["rounds"].append({
        "round": i, "id": d.name, "date": m["date"], "title": m["title"],
        "outfit_id": m["outfit_id"], "sketches": [x.get("sketch_id", "") for x in m["images"]],
        "base": b,
        "images": [{"file": x["file"], "view": x["view"], "prompt": x["prompt"], "md": f"{b}/{x['prompt']}"} for x in m["images"]],
        "lines": m.get("lines", []),
    })
    rows.append(f"| R{i:03d} | {m['title']} | " + " ".join(
        f"<img width=110 src=\"{b}/{x['file']}\">" for x in m["images"]) +
        f" | `{m['outfit_id']}` | `{m['images'][0].get('sketch_id','')}` 等 4 张 | {m['date']} | [本轮]({b}/README.md) |")

(root / "docs/data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme = root / "README.md"
t = readme.read_text(encoding="utf-8")
block = ("| 轮次 | 主题 | 四图预览 | 穿搭id | 线稿id | 日期 | 现场 |\n|---|---|---|---|---|---|---|\n"
         + "\n".join(rows[-10:]) + "\n")
t = re.sub(r"<!-- INDEX:START -->.*?<!-- INDEX:END -->",
           "<!-- INDEX:START -->\n" + block + "<!-- INDEX:END -->", t, flags=re.S)
readme.write_text(t, encoding="utf-8")

arch = ("# 全量轮次台账\n\n> 由 `tools/build_index.py` 生成，只追加，不手改。\n\n"
        "| 轮次 | 目录 | 主题 | 穿搭id | 日期 |\n|---|---|---|---|---|\n"
        + "\n".join(f"| R{i:03d} | `{d.name}` | {data['rounds'][i-1]['title']} | `{data['rounds'][i-1]['outfit_id']}` | {data['rounds'][i-1]['date']} |"
                     for i, d in enumerate(rounds, 1)) + "\n")
(root / "ARCHIVE.md").write_text(arch, encoding="utf-8")
print(f"校验通过：{len(rounds)} 轮，{len(rounds)*4} 图 {len(rounds)*4} md 全配对；索引与台账已回写。")
