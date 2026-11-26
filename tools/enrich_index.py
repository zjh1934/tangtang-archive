#!/usr/bin/env python3
"""唐唐归档仓 · 分类筛选索引重建器（v2）

与 docs/CONCURRENCY.md 的并发契约兼容：
  * 权威数据 = rounds/*/manifest.json + 同目录四份 NN_*.md，只增不改；
  * 本工具只重写「可再生派生文件」：docs/data.json、docs/index.html 的 DATA 行；
  * 不碰 README.md / ARCHIVE.md / tools/merge_index.py / tools/build_index.py /
    docs/CONCURRENCY.md / 任何轮次目录；
  * --push 走 CAS：base_tree 用远端最新 tree、PATCH force=False、提交前复核 ref，
    撞上另一个对话先提交就整轮重来。

用法：
  python3 tools/enrich_index.py --local                 # 扫本地仓库根目录，写回派生文件
  python3 tools/enrich_index.py --push                 # 从远端实时拉全量，CAS 推送派生文件
  python3 tools/enrich_index.py --self-test            # 校验生成物与 merge_index_html 兼容
"""
import argparse
import base64
import concurrent.futures
import importlib.util
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


def gallery_mod():
    """同目录加载唯一实现，保证本地副本与镜像副本共用一份生成逻辑。"""
    p = Path(__file__).resolve().parent / "gallery_md.py"
    spec = importlib.util.spec_from_file_location("tangtang_gallery_md", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

REPO = "zjh1934/tangtang-archive"
BRANCH = "main"
API = "https://api.github.com"
TOKEN_FILE = Path("/data/user_persistent_data/听本/.secrets/gh_token")
VIEWS = ["front", "side", "seat", "close"]
HAIR5 = ["蓬松披肩大波浪", "低侧马尾", "半扎发", "慵懒低盘发", "锁骨微卷"]
HAIR_PATTERNS = [("半扎发", r"半扎发|半扎"), ("低侧马尾", r"低侧马尾|侧马尾"),
                 ("慵懒低盘发", r"慵懒低盘发|低盘发|低髻"),
                 ("锁骨微卷", r"锁骨微卷|齐锁骨.{0,8}微卷|齐锁骨.{0,8}外卷"),
                 ("蓬松披肩大波浪", r"蓬松披肩大波浪|披肩大波浪")]
TAG_RULES = [("咖啡", "咖啡|豆子|拿铁|换豆|咖啡店"), ("口红", "口红|试色|唇膏|唇色"),
             ("卧室", "卧室|起床|赖床|床沿|枕套|枕头"), ("洗漱", "洗头|洗脸|洗漱|搪瓷|浴巾|毛巾按脸"),
             ("沙发", "沙发|薄毯|毛毯|毯子"), ("窗边", "推窗|白茶花|手帕|咳"),
             ("老街", "老街|路灯|唱片店|青石板|斑马线|巷口"),
             ("渡轮", "渡轮|江面|灯塔|芦苇|船票|甲板|石阶|候船"),
             ("亲亲", "亲亲|亲一下|凑过来亲|吻"), ("耳环", "耳环|耳饰|银饰摊"),
             ("街拍", "街拍|偷看|老街")]
SLUG_TAGS = {"coffee-beans": ["咖啡"], "lipstick-tryon": ["口红"], "morning-rise": ["卧室"],
             "coffee-and-earrings": ["咖啡", "耳环"], "tired-sofa-evening": ["沙发"],
             "fresh-window-care": ["窗边"], "wash-hair-errand": ["洗漱"],
             "morning-tea-wash": ["洗漱"], "evening-street-gaze": ["老街"],
             "ferry-lighthouse": ["渡轮"], "lovers-kiss": ["亲亲"]}


def token():
    raw = TOKEN_FILE.read_text(errors="ignore").strip()
    for l in raw.splitlines():
        l = l.strip()
        if not l or l.startswith("#"):
            continue
        if "=" in l:
            l = l.split("=", 1)[1].strip().strip('"').strip("'")
        if l:
            return l
    raise SystemExit("凭据文件里没取到 token")


def api(method, path, body=None, tok=None, timeout=90):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method,
        headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                 "User-Agent": "tangtang-enrich", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")


def remote_text(tok, path):
    code, j = api("GET", f"/repos/{REPO}/contents/{path}?ref={BRANCH}", tok=tok)
    if code != 200:
        return None
    return base64.b64decode(j["content"]).decode("utf-8")


def remote_tree(tok):
    code, ref = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}", tok=tok)
    if code != 200:
        raise SystemExit(f"读 main 失败 {code}: {ref}")
    head = ref["object"]["sha"]
    _, c = api("GET", f"/repos/{REPO}/git/commits/{head}", tok=tok)
    _, t = api("GET", f"/repos/{REPO}/git/trees/{c['tree']['sha']}?recursive=1", tok=tok)
    return head, c["tree"]["sha"], [x["path"] for x in t.get("tree", [])]


def split_md(text):
    m = re.search(r"##\s*终稿提示词\s*\n+```text\n(.*?)\n```", text, re.S)
    prompt = m.group(1).strip() if m else ""
    n = re.search(r"##\s*一句点评\s*\n+(.+?)(?:\n\n|\Z)", text, re.S)
    note = n.group(1).strip() if n else ""
    return prompt, note


def norm_hair(s):
    s = re.sub(r"(?:不是|并非|别把|而非|不锁死)[^，。；\n]{0,60}", "", s)
    scores = [(k, len(re.findall(p, s))) for k, p in HAIR_PATTERNS]
    best, n = max(scores, key=lambda x: x[1])
    return best if n else "未标注"


def derive(m, prompt_texts, notes, rid):
    blob = " ".join([m.get("title", ""), rid] + prompt_texts + m.get("lines", []))
    hair = m.get("hair") or norm_hair(blob)
    tags = m.get("tags")
    if not tags:
        slug = re.sub(r"^\d{8}[a-z]?_", "", rid)
        slug = re.sub(r"-\d+$", "", slug)
        tags = SLUG_TAGS.get(slug, [])[:]
        if not tags:
            hits = [(t, len(re.findall(rx, blob))) for t, rx in TAG_RULES]
            tags = [t for t, n in sorted(hits, key=lambda x: -x[1])[:2] if n >= 2]
    if not tags:
        tags = ["其它"]
    src = m.get("source") or ("lovers" if "lovers" in rid else "yuanbao")
    return {
        "round": m.get("round", 0), "id": rid, "date": m.get("date", ""),
        "title": m.get("title", ""), "theme": m.get("theme", ""),
        "outfit_id": m.get("outfit_id", ""), "month": (m.get("date") or "")[:7] or "—",
        "hair": hair, "tags": tags, "source": src,
        "sketches": [x.get("sketch_id", "") for x in m.get("images", [])],
        "seeds": [x.get("seed") for x in m.get("images", [])],
        "base": f"rounds/{rid}",
        "images": [{"file": x["file"], "view": x["view"], "prompt": x["prompt"],
                    "md": f"rounds/{rid}/{x['prompt']}"} for x in m["images"]],
        "lines": m.get("lines", []), "notes": notes, "prompt_texts": prompt_texts,
        "status": m.get("status", "final"),
    }


def collect_local(root):
    root = Path(root)
    out = []
    for d in sorted(p for p in (root / "rounds").iterdir() if p.is_dir() and not p.name.startswith("_")):
        m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
        pts, nts = [], []
        for im in m["images"]:
            t = (d / im["prompt"]).read_text(encoding="utf-8")
            p, n = split_md(t)
            pts.append(p); nts.append(n)
        out.append(derive(m, pts, nts, d.name))
    return out


def collect_remote(tok, paths):
    ids = sorted({p.split("/")[1] for p in paths if p.startswith("rounds/") and p.count("/") >= 2})
    need = []
    for rid in ids:
        need.append(f"rounds/{rid}/manifest.json")
        for p in paths:
            if p.startswith(f"rounds/{rid}/") and re.match(r"^\d\d_(front|side|seat|close)\.md$", p.split("/")[-1]):
                need.append(p)
    texts = {}
    def pull(p):
        t = remote_text(tok, p)
        return p, (t or "")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for p, t in ex.map(pull, need):
            texts[p] = t
    out = []
    for rid in ids:
        mp = f"rounds/{rid}/manifest.json"
        if not texts.get(mp):
            continue
        m = json.loads(texts[mp])
        pts, nts = [], []
        for im in m["images"]:
            p, n = split_md(texts.get(f"rounds/{rid}/{im['prompt']}", ""))
            pts.append(p); nts.append(n)
        out.append(derive(m, pts, nts, rid))
    return out


def make_data(rounds):
    now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
    return {"schema": 2, "gallery_version": 2, "repo": REPO, "updated_at": now, "rounds": rounds}


def render_html(template, data):
    line = "const DATA = " + json.dumps(data, ensure_ascii=False) + ";"
    assert "\n" not in line
    out, n = re.subn(r"^const DATA = .*;$", lambda _: line, template, count=1, flags=re.M)
    assert n == 1, "模板里没找到 const DATA = __DATA__; 单行"
    return out


def cas_push(tok, build_fn, msg, retries=5):
    """每次重试都先用这一刻的远端 tree 重新 build_fn 生成文件，杜绝拿旧快照覆盖对方新轮。"""
    for attempt in range(1, retries + 1):
        head, base_tree, paths = remote_tree(tok)
        files, rounds = build_fn(tok, paths)
        entries = []
        for path, blob in files.items():
            code, r = api("POST", f"/repos/{REPO}/git/blobs",
                          {"content": base64.b64encode(blob).decode(), "encoding": "base64"}, tok=tok)
            if code not in (200, 201):
                raise SystemExit(f"blob 失败 {path} {code}: {r}")
            entries.append({"path": path, "mode": "100644", "type": "blob", "sha": r["sha"]})
        code, tr = api("POST", f"/repos/{REPO}/git/trees",
                       {"tree": entries, "base_tree": base_tree}, tok=tok)
        if code not in (200, 201):
            raise SystemExit(f"tree 失败 {code}: {tr}")
        code, cm = api("POST", f"/repos/{REPO}/git/commits",
                       {"message": msg, "tree": tr["sha"], "parents": [head]}, tok=tok)
        if code not in (200, 201):
            raise SystemExit(f"commit 失败 {code}: {cm}")
        # PATCH 前复核 ref 没被另一个对话顶掉
        code2, ref2 = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}", tok=tok)
        if code2 == 200 and ref2["object"]["sha"] != head:
            print(f"第 {attempt} 次：远端 ref 已变（对方先提交），重取重算")
            continue
        code, rr = api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}",
                       {"sha": cm["sha"], "force": False}, tok=tok)
        if code in (200, 201):
            # 提交后校验：对方最近一轮目录仍完好
            _, _, after = remote_tree(tok)
            lost = [p for p in paths if p.startswith(("rounds/", "letters/")) and p not in after]
            assert not lost, f"提交后丢了远端文件：{lost[:5]}"
            return cm["sha"], paths, rounds
        print(f"第 {attempt} 次 PATCH 冲突（{code}），重试")
    raise SystemExit("CAS 重试次数用尽，未提交；稍后再跑一次即可")


def self_test():
    tpl = (Path(__file__).resolve().parent / "gallery_template.html").read_text(encoding="utf-8")
    imgs = [{"file": f"{i:02d}_{v}.png", "view": v, "prompt": f"{i:02d}_{v}.md"}
            for i, v in enumerate(["front", "side", "seat", "close"], 1)]
    d = make_data([{"round": 1, "id": "x", "base": "rounds/x", "images": imgs,
                    "tags": ["渡轮"], "lines": ["一句话"]}])
    h = render_html(tpl, d)
    assert re.search(r"^const DATA = \{.*\};$", h, re.M), "DATA 行不满足 merge_index_html 正则"
    # 与另一个对话的 merge_index_html 同规则验证替换
    line = "const DATA = " + json.dumps(d, ensure_ascii=False) + ";"
    h2, n = re.subn(r"^const DATA = \{.*\};$", lambda _: line, h, count=1, flags=re.M)
    assert n == 1 and h2 == h
    assert "id=\"fHair\"" in h and "id=\"tabs\"" in h and "单图图鉴" in h
    # 防回归：CAS 每次重试都必须重新全量收集，不能拿旧快照覆盖对方新轮
    src = Path(__file__).read_text(encoding="utf-8")
    loop = src[src.index("def cas_push"):src.index("def self_test")]
    assert "for attempt in" in loop and "build_fn(tok, paths)" in loop
    assert loop.index("for attempt in") < loop.index("build_fn(tok, paths)")
    gm = gallery_mod()
    g = gm.gallery_md(d)
    assert "![" in g and all(k in g for k in ("按轮看", "按场景", "按发型", "按月份"))
    b = gm.banner(d)
    assert "GALLERY.md" in b and "<img" in b
    assert gm.merge_banner(gm.merge_banner("# T\n<!-- INDEX:START -->\n| R001 | 旧 |\n<!-- INDEX:END -->\n", b), b) \
        == gm.merge_banner("# T\n<!-- INDEX:START -->\n| R001 | 旧 |\n<!-- INDEX:END -->\n", b)
    print("self-test OK：DATA 单行兼容 merge_index_html；分类/筛选控件齐全；CAS 重试重跑全量收集；画廊与主页横幅幂等")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--local", action="store_true", help="扫本地仓库根目录，写回派生文件")
    ap.add_argument("--push", action="store_true", help="从远端实时拉全量，CAS 推送派生文件")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--root", default=".", help="本地仓库根目录（--local 用）")
    a = ap.parse_args()
    if a.self_test:
        self_test(); return
    if not (a.local or a.push):
        ap.print_help(); return

    tpl_path = Path(__file__).resolve().parent / "gallery_template.html"
    tpl = tpl_path.read_text(encoding="utf-8")
    gm = gallery_mod()
    if a.local:
        rounds = collect_local(a.root)
        data = make_data(rounds)
        root = Path(a.root)
        (root / "docs" / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (root / "docs" / "index.html").write_text(render_html(tpl, data), encoding="utf-8")
        (root / "GALLERY.md").write_text(gm.gallery_md(data), encoding="utf-8")
        rp = root / "README.md"
        rp.write_text(gm.merge_banner(rp.read_text(encoding="utf-8"), gm.banner(data)), encoding="utf-8")
        print(f"本地重建：{len(rounds)} 轮，{sum(len(r['images']) for r in rounds)} 张图；"
              "docs/data.json、docs/index.html、GALLERY.md 与 README 主页横幅已写回")
        return

    tok = token()
    handoff = (Path(__file__).resolve().parent.parent / "docs" / "HANDOFF.md")

    def build_all(_tok, paths):
        rs = collect_remote(_tok, paths)
        assert len(rs) >= 1 and all(len(r["images"]) == 4 for r in rs), "远端轮次或四图配对异常"
        data = make_data(rs)
        # README 是共享索引：从「此刻远端正文」出发只幂等替换横幅块，INDEX 块一字不动
        readme_now = remote_text(_tok, "README.md") or ""
        gm = gallery_mod()
        return {
            "docs/data.json": (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
            "docs/index.html": render_html(tpl, data).encode("utf-8"),
            "GALLERY.md": gm.gallery_md(data).encode("utf-8"),
            "README.md": gm.merge_banner(readme_now, gm.banner(data)).encode("utf-8"),
            "docs/HANDOFF.md": handoff.read_bytes(),
            "tools/enrich_index.py": Path(__file__).read_bytes(),
            "tools/gallery_template.html": tpl_path.read_bytes(),
            "tools/gallery_md.py": (Path(__file__).resolve().parent / "gallery_md.py").read_bytes(),
        }, rs

    sha, before, rounds = cas_push(tok, build_all, "chore: 画廊 v2（分类/筛选/看图）+ 分类索引重建 | source=yuanbao")
    print(f"推送成功 | commit {sha[:8]} | {len(rounds)} 轮 {sum(len(r['images']) for r in rounds)} 张图 | 远端原有 {len([p for p in before if p.startswith('rounds/')])} 个轮次文件全部保留")
    print("README 只幂等替换 GALLERY 横幅块，INDEX 块与 ARCHIVE.md / docs/CONCURRENCY.md / "
          "tools/merge_index.py / tools/build_index.py / 任何轮次目录 / letters/ 均未触碰")


if __name__ == "__main__":
    main()
