#!/usr/bin/env python3
"""唐唐归档仓 · GitHub 原生渲染画廊与主页横幅生成器。

GitHub 出于安全不把仓库里的 .html 渲染成网页（点开只显示源码），私有仓 Free 套餐
也开不了 Pages。所以真正的「在仓库网页上直接看图」走 Markdown：GALLERY.md 里用
相对路径 <img> 嵌四图，GitHub 登录后直接渲染；README.md 顶部用横幅把入口顶到第一屏。

本模块是唯一实现，tools/ 本地副本与 archive_repo/tools/ 镜像副本同 hash；
archive_round.py（每轮归档）与 enrich_index.py（索引自愈）都从它生成，确定性一致。
GALLERY.md 与 README 横幅都是**可再生派生文件**，只由远端此刻全量数据生成，
CAS 重试时重算，不占四个共享索引、不改 rounds/ 任何历史。

    python3 tools/gallery_md.py --self-test
"""
import re
import sys
from collections import defaultdict

MARK_START = "<!-- GALLERY:START -->"
MARK_END = "<!-- GALLERY:END -->"
VIEWS = ["front", "side", "seat", "close"]
VIEW_CN = {"front": "正面", "side": "侧身", "seat": "坐姿", "close": "特写"}


def _r(r):
    """兼容 enrich 全量 entry 与对方归档时只带 9 个基础字段的简版 entry。"""
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


def _img(r, im, width=220, link=True):
    """GitHub Markdown 里相对路径 <img> 会被渲染成登录可见的原图，不用另存缩略图。"""
    src = f"{r['base']}/{im['file']}"
    tag = f'<img width="{width}" src="{src}" alt="{im.get("view","")}">'
    return f"[{tag}]({src})" if link else tag


def banner(data):
    """README 第一屏：大入口 + 最近两轮八张图预览墙；幂等标记块，不碰 INDEX 块。"""
    rounds = sorted(data.get("rounds", []), key=lambda x: x.get("id", ""))
    n_img = sum(len(_r(x)["images"]) for x in rounds)
    recent = rounds[-2:][::-1]
    cells = []
    for x in recent:
        r = _r(x)
        for im in r["images"][:4]:
            cells.append(f'<a href="{r["base"]}/{im["file"]}"><img width="118" src="{r["base"]}/{im["file"]}" alt="{im.get("view","")}"></a>')
    wall = " ".join(cells) if cells else "_（还没有终稿图）_"
    return f"""{MARK_START}
# 🎨 唐唐 · 逐轮终稿画廊

## 👉 [**点这里进画廊 · GALLERY.md · {len(rounds)} 轮 {n_img} 张终稿图直接看**](GALLERY.md) 👈

{wall}

> 上面是最近两轮，点图看原图。画廊里按**场景 / 发型 / 月份**分组、每轮四张大图横排、每图配同名终稿 prompt md。
> 交互式下拉筛选与灯箱：把仓库克隆下来双击 [docs/index.html](docs/index.html)（GitHub 网页只显示 HTML 源码，不渲染成网页）。
> 全量台账 [ARCHIVE.md](ARCHIVE.md) ｜ 两个对话的留言区 [letters/](letters/README.md)
{MARK_END}"""


def merge_banner(readme_text, banner_text):
    """幂等替换横幅块；对方 merge_readme 只动 INDEX 块内部，横幅在块外不会被吃掉。"""
    pat = re.escape(MARK_START) + r".*?" + re.escape(MARK_END)
    if re.search(pat, readme_text, re.S):
        return re.sub(pat, lambda _: banner_text.strip(), readme_text, count=1, flags=re.S)
    return banner_text + "\n\n" + readme_text.lstrip("\n")


def _round_block(x, open_by_default=False, width=220):
    r = _r(x)
    ims = r["images"][:4]
    head = "| " + " | ".join(f"{i+1:02d} {VIEW_CN.get(im.get('view',''),im.get('view',''))}" for i, im in enumerate(ims)) + " |"
    sep = "|" + "---|" * len(ims)
    row = "| " + " | ".join(_img(r, im, width) for im in ims) + " |"
    prompts = " · ".join(
        f"[{i+1:02d} prompt]({r['base']}/{im['prompt']})" for i, im in enumerate(ims))
    chips = " · ".join([f"`{r['outfit_id']}`", r["hair"]] + r["tags"] + [r["month"], f"source={r['source']}"])
    lines = "<br>".join(f"{i+1}. {t}" for i, t in enumerate(r["lines"])) or "—"
    meta = (f"**R{r['round']:03d} · {r['title']}**　{chips}<br>"
            f"[本轮现场]({r['base']}/README.md) ｜ [manifest]({r['base']}/manifest.json) ｜ {prompts}")
    body = "\n".join([head, sep, row, "", meta, "", lines])
    op = " open" if open_by_default else ""
    return f"<details{op}>\n<summary><b>R{r['round']:03d} · {r['title']}</b>　{r['hair']} · {'、'.join(r['tags'])}</summary>\n\n{body}\n\n</details>\n"


def _group(title, anchor, rounds, keyfn, width=110):
    g = defaultdict(list)
    for x in rounds:
        r = _r(x)
        keys = keyfn(r) or ["其它"]
        for k in keys:
            g[k].append(r)
    out = [f'<a id="{anchor}"></a>\n\n## {title}\n']
    for k in sorted(g, key=lambda s: (-len(g[s]), s)):
        rs = sorted(g[k], key=lambda r: r["id"], reverse=True)
        out.append(f"\n### {k} · {len(rs)} 轮\n")
        out.append("| 轮次 | 封面 | 其余三张 | 提示词 |\n|---|---|---|---|\n")
        for r in rs:
            ims = r["images"][:4]
            if not ims:
                continue
            first = _img(r, ims[0], width)
            rest = " ".join(_img(r, im, width) for im in ims[1:])
            pr = f"[{r['id']}/]({r['base']}/README.md)"
            out.append(f"| R{r['round']:03d} {r['title']} | {first} | {rest} | {pr} |\n")
    return "\n".join(out)


def gallery_md(data):
    """完整 GALLERY.md：GitHub 网页原生渲染，图片直接可见；不依赖 Pages、不依赖 JS。"""
    rounds = sorted(data.get("rounds", []), key=lambda x: x.get("id", ""))
    n_img = sum(len(_r(x)["images"]) for x in rounds)
    newest = rounds[-1] if rounds else None
    parts = [
        "# 🎨 唐唐 · 终稿画廊（网页直接看图）\n",
        "> 每一张图都由 GitHub 直接渲染，**点图看原图**，点 prompt 看同目录同名终稿提示词。\n"
        "> 按场景 / 发型 / 月份分组，往下滑就行；要下拉筛选与灯箱，克隆仓库后双击 `docs/index.html`\n"
        "> （私有仓 Free 套餐开不了 Pages，GitHub 网页只显示 HTML 源码，不会把 `.html` 渲染成网页）。\n",
        f"**共 {len(rounds)} 轮 · {n_img} 张终稿图**　"
        "[最新一轮](#最新一轮) · [按轮看](#按轮看) · [按场景](#按场景) · "
        "[按发型](#按发型) · [按月份](#按月份) · [全量台账](ARCHIVE.md) · [回主页](README.md)\n",
        '<a id="最新一轮"></a>\n\n## 最新一轮\n',
    ]
    if newest:
        parts.append(_round_block(newest, open_by_default=True, width=240))
    parts.append('<a id="按轮看"></a>\n\n## 按轮看（新→旧，每轮四张）\n')
    for i, x in enumerate(reversed(rounds)):
        parts.append(_round_block(x, open_by_default=(i < 2)))
    parts.append(_group("按场景", "按场景", rounds, lambda r: r["tags"]))
    parts.append(_group("按发型", "按发型", rounds, lambda r: [r["hair"]]))
    parts.append(_group("按月份", "按月份", rounds, lambda r: [r["month"]]))
    parts.append("\n---\n\n> 只增不改：本页由 `tools/enrich_index.py --push` 从 `rounds/*/manifest.json` 与四份 md 全量重建，"
                 "两个对话都能跑，CAS 安全；历史轮次与四份 prompt md 一个不动。\n")
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
    assert "GALLERY.md" in b and b.count("<img") == 8
    g = gallery_md(d)
    assert g.count("<img") >= 8 and "按场景" in g and "按发型" in g and "按月份" in g
    assert "rounds/20261126a_a/01_front.png" in g and "01_front.md" in g
    readme = "# 唐唐\n\n<!-- INDEX:START -->\n| R001 | 旧 |\n<!-- INDEX:END -->\n尾\n"
    once = merge_banner(readme, b)
    twice = merge_banner(once, b)
    assert once == twice, "横幅必须幂等"
    assert "<!-- INDEX:START -->" in once and "| R001 | 旧 |" in once and "尾" in once
    # 对方 merge_readme 只动 INDEX 块内部，横幅必须活下来
    import importlib.util
    from pathlib import Path
    p = Path(__file__).resolve().parent / "merge_index.py"
    if p.exists():
        spec = importlib.util.spec_from_file_location("mi", p)
        mi = importlib.util.module_from_spec(spec); spec.loader.exec_module(mi)
        after = mi.merge_readme(once, "| R003 | 新 | <img src=\"rounds/x/01_front.png\"> |")
        assert MARK_START in after and "GALLERY.md" in after and "| R003 | 新 |" in after
    print("self-test OK：画廊 44 图可见 / 主页横幅幂等 / INDEX 块与对方合并器不打架")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        print(__doc__)
