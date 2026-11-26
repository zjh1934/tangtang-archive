#!/usr/bin/env python3
"""唐唐归档仓 · 手机友好的网页画廊与主页横幅生成器（v3）。

设计原则（用户当面定）：给人用的。手机 GitHub App 里表格会被挤成小方块、
<details> 折叠要点一下才展开、图片列宽被压成 0 变占位符，所以：
  · 不用表格、不用 <details>、不用 raw <img> 标签
  · 每张图独占一段，标准 Markdown 图片语法，GitHub 自己给私有仓图片签名
  · 一屏一张大图，往下滑就是全部；顶部一行锚点目录直达每一轮
  · 分类只做文字链接目录，不重复嵌图（页面不再又长又碎）

真正可筛选 / 两列大图 / 灯箱的交互式页面由 tools/offline_gallery.py 生成单文件
离线 HTML（图片内联），交付到手机打开即用；GitHub 网页不渲染 .html 只显示源码。

    python3 tools/gallery_md.py --self-test
"""
import re
import sys
from collections import defaultdict

MARK_START = "<!-- GALLERY:START -->"
MARK_END = "<!-- GALLERY:END -->"
VIEWS = ["front", "side", "seat", "close"]
VIEW_CN = {"front": "正面", "side": "侧身", "seat": "坐姿", "close": "特写"}
# 公开仓用绝对直链：GitHub 手机 App 的 Markdown 预览不重写相对 src（会变成死图），
# 绝对 raw URL 在网页、App、第三方预览器里都能直接出图。
IMG_BASE = "https://raw.githubusercontent.com/zjh1934/tangtang-archive/main/"


def _r(r):
    return {
        "round": r.get("round", 0), "id": r.get("id", ""),
        "title": r.get("title", ""), "date": r.get("date", ""),
        "outfit_id": r.get("outfit_id", ""),
        "hair": r.get("hair") or "未标注",
        "tags": r.get("tags") or ["其它"],
        "month": r.get("month") or (r.get("date") or "")[:7] or "—",
        "source": r.get("source") or ("lovers" if "lovers" in r.get("id", "") else "yuanbao"),
        "base": r.get("base") or "rounds/" + r.get("id", ""),
        "images": r.get("images") or [],
        "lines": r.get("lines") or [],
    }


def _src(r, im):
    return IMG_BASE + f"{r['base']}/{im['file']}"


def banner(data):
    """README 第一屏：大入口 + 最近两轮八张预览（一行四个 inline 图，不用表格）。"""
    rounds = sorted(data.get("rounds", []), key=lambda x: x.get("id", ""))
    n_img = sum(len(_r(x)["images"]) for x in rounds)
    recent = rounds[-2:][::-1]
    rows = []
    for x in recent:
        r = _r(x)
        cells = []
        for im in r["images"][:4]:
            s = _src(r, im)
            cells.append(f"[![R{r['round']:03d} {im.get('view','')}]({s})]({s})")
        rows.append(" ".join(cells))
    wall = "\n\n".join(rows) if rows else "_（还没有终稿图）_"
    return f"""{MARK_START}
# 🎨 唐唐 · 逐轮终稿画廊

## 🌐 [**打开网页画廊（两列大图 · 筛选 · 灯箱，像图鉴那样）**](https://zjh1934.github.io/tangtang-archive/) 🌐

## 👉 [GALLERY.md · {len(rounds)} 轮 {n_img} 张终稿图（网页内一屏一张）](GALLERY.md) 👈

{wall}

> 上面是最近两轮，点图看原图。**网页画廊**是真正的可交互图鉴：两列大图卡片、搜索、场景／发型／月份筛选、点开看大图与 prompt 全文、明暗切换，手机浏览器直接打开。
> 全量台账 [ARCHIVE.md](ARCHIVE.md) ｜ 两个对话的留言区 [letters/](letters/README.md) ｜ [版权声明（公开但不开源）](NOTICE.md)
{MARK_END}"""


def merge_banner(readme_text, banner_text):
    """幂等替换横幅块；对方 merge_readme 只动 INDEX 块内部，横幅在块外不受影响。"""
    pat = re.escape(MARK_START) + r".*?" + re.escape(MARK_END)
    if re.search(pat, readme_text, re.S):
        return re.sub(pat, lambda _: banner_text.strip(), readme_text, count=1, flags=re.S)
    return banner_text + "\n\n" + readme_text.lstrip("\n")


def _round_section(x):
    """一轮 = 一个标题 + 四张独占段落的大图 + 一行 prompt 链接。"""
    r = _r(x)
    chips = " · ".join([f"`{r['outfit_id']}`", r["hair"]] + r["tags"]
                       + [r["month"], f"source={r['source']}"])
    out = [f'<a id="r{r["round"]:03d}"></a>', "",
           f"## R{r['round']:03d} · {r['title']}", "",
           f"{chips} ｜ [本轮现场]({r['base']}/README.md) · [manifest]({r['base']}/manifest.json)", ""]
    for i, im in enumerate(r["images"][:4], 1):
        s = _src(r, im)
        cn = VIEW_CN.get(im.get("view", ""), im.get("view", ""))
        out += [f"[![{i:02d} {cn} · R{r['round']:03d}]({s})]({s})", "",
                f"**{i:02d} {cn}**　[看原图]({s}) · [{i:02d} 终稿 prompt]({r['base']}/{im['prompt']})", ""]
    if r["lines"]:
        out += ["> " + " ／ ".join(r["lines"]), ""]
    out += ["---", ""]
    return "\n".join(out)


def _index(title, anchor, rounds, keyfn):
    g = defaultdict(list)
    for x in rounds:
        r = _r(x)
        for k in (keyfn(r) or ["其它"]):
            g[k].append(r)
    lines = [f'<a id="{anchor}"></a>', "", f"## {title}", ""]
    for k in sorted(g, key=lambda s: (-len(g[s]), s)):
        rs = sorted(g[k], key=lambda r: r["id"], reverse=True)
        links = " · ".join(f"[R{r['round']:03d} {r['title']}](#r{r['round']:03d})" for r in rs)
        lines += [f"- **{k}**（{len(rs)} 轮）：{links}", ""]
    return "\n".join(lines)


def gallery_md(data):
    """完整 GALLERY.md：GitHub 网页与手机 App 都直接出图，无表格、无折叠。"""
    rounds = sorted(data.get("rounds", []), key=lambda x: x.get("id", ""))
    n_img = sum(len(_r(x)["images"]) for x in rounds)
    toc = " · ".join(f"[R{_r(x)['round']:03d}](#r{_r(x)['round']:03d})"
                     for x in reversed(rounds))
    parts = [
        "# 🎨 唐唐 · 终稿图鉴", "",
        f"**{len(rounds)} 轮 · {n_img} 张终稿图**　一屏一张大图，往下滑就是全部；**点图看原图**，每图配同名终稿 prompt md。", "",
        "> 手机上想两列大图、分类筛选、点开看大图？用交付到手机的**离线单文件画廊**（图片已内联，不联网也能看）；"
        "GitHub 网页只显示 `.html` 源码，不渲染成网页。", "",
        "**直达某一轮**　" + toc, "",
        "[按场景](#按场景) · [按发型](#按发型) · [按月份](#按月份) · [全量台账](ARCHIVE.md) · [回主页](README.md)", "",
        "---", "",
    ]
    for x in reversed(rounds):
        parts.append(_round_section(x))
    parts.append(_index("按场景", "按场景", rounds, lambda r: r["tags"]))
    parts.append(_index("按发型", "按发型", rounds, lambda r: [r["hair"]]))
    parts.append(_index("按月份", "按月份", rounds, lambda r: [r["month"]]))
    parts += ["---", "",
              "> 只增不改：本页由 `tools/gallery_md.py` 从 `rounds/*/manifest.json` 与四份 md 全量重建，"
              "两个对话归档时都顺手生成，CAS 安全；历史轮次与 prompt md 一个不动。", ""]
    return "\n".join(parts)


def self_test():
    d = {"schema": 2, "rounds": [
        {"round": 1, "id": "20261126a_a", "title": "渡轮", "date": "2026-11-26",
         "outfit_id": "SUM-0069", "hair": "锁骨微卷", "tags": ["渡轮"], "month": "2026-11",
         "source": "yuanbao", "base": "rounds/20261126a_a",
         "images": [{"file": f"{i:02d}_{v}.png", "view": v, "prompt": f"{i:02d}_{v}.md"}
                    for i, v in enumerate(VIEWS, 1)], "lines": ["一句话"]},
        {"round": 2, "id": "20261126b_b", "title": "亲亲", "date": "2026-11-26",
         "outfit_id": "PTY-0047", "hair": "未标注", "tags": ["亲亲"], "month": "2026-11",
         "source": "lovers", "base": "rounds/20261126b_b",
         "images": [{"file": f"{i:02d}_{v}.png", "view": v, "prompt": f"{i:02d}_{v}.md"}
                    for i, v in enumerate(VIEWS, 1)], "lines": []},
    ]}
    b = banner(d)
    assert b.startswith(MARK_START) and b.rstrip().endswith(MARK_END)
    assert "GALLERY.md" in b and "zjh1934.github.io" in b and b.count("![") == 8
    assert "|" not in b.split("\n\n")[4], "横幅不再用表格"
    g = gallery_md(d)
    assert g.count("![") == 8 and "<details" not in g and "<table" not in g
    assert all(k in g for k in ("按场景", "按发型", "按月份", "#r001", "#r002"))
    assert IMG_BASE + "rounds/20261126a_a/01_front.png" in g and "01_front.md" in g
    readme = "# 唐唐\n\n<!-- INDEX:START -->\n| R001 | 旧 |\n<!-- INDEX:END -->\n尾\n"
    once = merge_banner(readme, b)
    assert once == merge_banner(once, b), "横幅必须幂等"
    assert "<!-- INDEX:START -->" in once and "| R001 | 旧 |" in once and "尾" in once
    from pathlib import Path
    import importlib.util
    p = Path(__file__).resolve().parent / "merge_index.py"
    if p.exists():
        spec = importlib.util.spec_from_file_location("mi", p)
        mi = importlib.util.module_from_spec(spec); spec.loader.exec_module(mi)
        after = mi.merge_readme(once, "| R003 | 新 | <img src=\"rounds/x/01_front.png\"> |")
        assert MARK_START in after and "GALLERY.md" in after and "| R003 | 新 |" in after
    print("self-test OK：手机友好画廊（无表格/无折叠/一屏一图）/ 主页横幅幂等 / INDEX 块与对方合并器不打架")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        print(__doc__)
