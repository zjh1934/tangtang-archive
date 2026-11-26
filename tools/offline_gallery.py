#!/usr/bin/env python3
"""唐唐 · 终稿图鉴离线单文件 HTML（图片内联，手机打开即用）。

GitHub 网页不渲染仓库里的 .html，私有仓 Free 套餐也开不了 Pages，所以把交互式
画廊做成**一个自包含 HTML 文件**交付到手机：44 张图压成内联缩略图，无 CDN、无网络、
不依赖仓库登录，浏览器/文件管理器点开就是两列大图卡片 + 搜索 + 分类筛选 + 灯箱。

数据来自 archive_repo/docs/data.json 与 rounds/*/*.png、*.md，与网页 GALLERY.md 同源。

    python3 tools/offline_gallery.py --root archive_repo --out 唐唐终稿图鉴.html
    python3 tools/offline_gallery.py --self-test
"""
import argparse
import base64
import html
import io
import json
import re
import sys
from pathlib import Path

from PIL import Image

THUMB_W = 560
VIEW_CN = {"front": "正面", "side": "侧身", "seat": "坐姿", "close": "特写"}


def thumb(path):
    """等比缩到宽 560 的 JPEG，转 data URI；原图 2.6MB → 约 60KB。"""
    with Image.open(path) as im:
        im = im.convert("RGB")
        w, h = im.size
        im = im.resize((THUMB_W, round(h * THUMB_W / w)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=80, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def collect(root):
    root = Path(root)
    data = json.loads((root / "docs" / "data.json").read_text(encoding="utf-8"))
    items, rounds_meta = [], []
    for r in sorted(data["rounds"], key=lambda x: x["id"], reverse=True):
        base = root / r["base"]
        meta = {
            "round": r.get("round", 0), "id": r.get("id", ""), "title": r.get("title", ""),
            "hair": r.get("hair") or "未标注", "tags": r.get("tags") or ["其它"],
            "month": r.get("month") or "—", "outfit": r.get("outfit_id", ""),
            "source": r.get("source", ""), "lines": r.get("lines") or [],
            "readme": (base / "README.md").read_text(encoding="utf-8") if (base / "README.md").exists() else "",
        }
        rounds_meta.append(meta)
        for i, im in enumerate(r.get("images", []), 1):
            p = base / im["file"]
            md = base / im["prompt"]
            if not p.exists():
                continue
            items.append({
                "n": len(items), "src": thumb(p), "round": meta["round"], "title": meta["title"],
                "id": meta["id"], "slot": f"{i:02d} {VIEW_CN.get(im.get('view', ''), im.get('view', ''))}",
                "hair": meta["hair"], "tags": meta["tags"], "month": meta["month"],
                "outfit": meta["outfit"], "source": meta["source"],
                "prompt": md.read_text(encoding="utf-8") if md.exists() else "（暂无 prompt）",
                "lines": meta["lines"],
            })
    return items, rounds_meta


def render(items, rounds_meta):
    payload = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tags = sorted({t for x in items for t in x["tags"]})
    hairs = sorted({x["hair"] for x in items})
    months = sorted({x["month"] for x in items}, reverse=True)

    def opts(xs):
        return "".join(f'<option value="{html.escape(v)}">{html.escape(v)}</option>' for v in xs)

    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>唐唐 · 终稿图鉴</title>
<style>
:root{{--bg:#0f1113;--card:#191c20;--fg:#eceae4;--sub:#8d9299;--acc:#e8739b;--line:#2a2e34;--chip:#22262b}}
html[data-t="light"]{{--bg:#faf9f6;--card:#fff;--fg:#22252a;--sub:#767b82;--acc:#c2416c;--line:#e5e2dc;--chip:#f0eeea}}
*{{box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
body{{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}}
header{{padding:22px 18px 10px;position:sticky;top:0;z-index:20;background:var(--bg);border-bottom:1px solid var(--line)}}
.kicker{{font-size:11px;letter-spacing:.22em;color:var(--sub);text-transform:uppercase}}
h1{{margin:6px 0 3px;font-size:25px;letter-spacing:.04em}}
.sub{{font-size:12px;color:var(--sub);line-height:1.6}}
.tabs{{display:flex;gap:8px;overflow-x:auto;padding:12px 18px 0;scrollbar-width:none}}
.tabs::-webkit-scrollbar{{display:none}}
.tab{{flex:0 0 auto;padding:8px 15px;border-radius:999px;background:var(--chip);color:var(--sub);font-size:13px;border:1px solid var(--line);cursor:pointer}}
.tab.on{{background:var(--acc);color:#fff;border-color:var(--acc)}}
.tools{{display:flex;gap:8px;padding:12px 18px;flex-wrap:wrap}}
input[type=search],select{{background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:13px;outline:none}}
input[type=search]{{flex:1 1 100%}}
select{{flex:1 1 30%;min-width:96px}}
.count{{padding:0 18px 10px;font-size:12px;color:var(--sub)}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:0 12px 40px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;cursor:pointer}}
.card img{{width:100%;display:block;aspect-ratio:9/16;object-fit:cover;background:#000}}
.card .m{{padding:9px 10px 11px}}
.card .r{{font-size:11px;color:var(--acc);font-weight:700;letter-spacing:.04em}}
.card .t{{font-size:12px;margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.card .g{{font-size:10px;color:var(--sub);margin-top:5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.empty{{grid-column:1/-1;text-align:center;color:var(--sub);padding:60px 0;font-size:14px}}
#lb{{position:fixed;inset:0;background:rgba(0,0,0,.96);z-index:50;display:none;flex-direction:column}}
#lb.on{{display:flex}}
#lbTop{{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;color:#fff;font-size:13px}}
#lbTop button{{background:#2a2e34;color:#fff;border:0;border-radius:9px;padding:8px 14px;font-size:13px}}
#lbImg{{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;padding:0 8px}}
#lbImg img{{max-width:100%;max-height:100%;object-fit:contain;border-radius:6px}}
#lbInfo{{max-height:34%;overflow:auto;padding:12px 16px 24px;color:#d8d6d1;font-size:12px;line-height:1.75;border-top:1px solid #2a2e34}}
#lbInfo b{{color:#fff}}
#lbInfo pre{{white-space:pre-wrap;word-break:break-word;font-family:inherit;margin:8px 0 0;color:#b9bdc3}}
.nav{{display:flex;gap:10px;justify-content:center;padding:8px}}
.nav button{{flex:1;max-width:140px;background:#2a2e34;color:#fff;border:0;border-radius:9px;padding:10px;font-size:14px}}
#themeBtn{{position:fixed;right:14px;bottom:18px;z-index:30;width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:var(--card);color:var(--fg);font-size:17px}}
</style></head><body>
<header>
 <div class="kicker">TANGTANG · FINAL FRAMES</div>
 <h1>唐唐 · 终稿图鉴</h1>
 <div class="sub">{len(rounds_meta)} 轮 · {len(items)} 张终稿图　两列大图，点开看全屏与终稿 prompt<br>图片已内联，不联网也能看 · 数据来自归档仓 rounds/</div>
</header>
<div class="tabs" id="tabs"></div>
<div class="tools">
 <input type="search" id="q" placeholder="搜轮次 / 标题 / 穿搭 id / 发型 / 场景">
 <select id="fTag"><option value="">全部场景</option>{opts(tags)}</select>
 <select id="fHair"><option value="">全部发型</option>{opts(hairs)}</select>
 <select id="fMonth"><option value="">全部月份</option>{opts(months)}</select>
</div>
<div class="count" id="count"></div>
<div class="grid" id="grid"></div>
<button id="themeBtn" title="切换明暗">◐</button>
<div id="lb">
 <div id="lbTop"><span id="lbTitle"></span><button onclick="closeLB()">关闭 ✕</button></div>
 <div id="lbImg"><img id="lbBig" src="" alt=""></div>
 <div class="nav"><button onclick="step(-1)">← 上一张</button><button onclick="step(1)">下一张 →</button></div>
 <div id="lbInfo"></div>
</div>
<script>
const DATA={payload};
let view='全部',cur=0,shown=DATA.slice();
const $=s=>document.querySelector(s);
const groups=[['全部',x=>true],['按轮看',x=>true],['按场景',x=>true],['按发型',x=>true],['按月份',x=>true]];
$('#tabs').innerHTML=groups.map(([n])=>`<button class="tab${{n==='全部'?' on':''}}" data-v="${{n}}">${{n}}</button>`).join('');
$('#tabs').onclick=e=>{{const b=e.target.closest('.tab');if(!b)return;view=b.dataset.v;
 document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('on',x===b));render();}};
function esc(s){{return String(s).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}})[c]);}}
function match(x){{
 const q=$('#q').value.trim().toLowerCase();
 const tag=$('#fTag').value,hair=$('#fHair').value,mon=$('#fMonth').value;
 if(tag&&!x.tags.includes(tag))return false;
 if(hair&&x.hair!==hair)return false;
 if(mon&&x.month!==mon)return false;
 if(q&&!(x.title+' '+x.id+' '+x.outfit+' '+x.hair+' '+x.tags.join(' ')+' '+x.slot).toLowerCase().includes(q))return false;
 return true;
}}
function render(){{
 shown=DATA.filter(match);
 if(view==='按轮看')shown.sort((a,b)=>b.round-a.round||a.n-b.n);
 else if(view==='按场景')shown.sort((a,b)=>a.tags.join().localeCompare(b.tags.join())||a.n-b.n);
 else if(view==='按发型')shown.sort((a,b)=>a.hair.localeCompare(b.hair)||a.n-b.n);
 else if(view==='按月份')shown.sort((a,b)=>b.month.localeCompare(a.month)||a.n-b.n);
 else shown.sort((a,b)=>a.n-b.n);
 $('#count').textContent=`共 ${{shown.length}} 张 · 当前「${{view}}」`;
 $('#grid').innerHTML=shown.length?shown.map(x=>`<div class="card" data-n="${{x.n}}"><img src="${{x.src}}" alt="${{esc(x.slot)}}" loading="lazy"><div class="m"><div class="r">R${{String(x.round).padStart(3,'0')}} · ${{esc(x.slot)}}</div><div class="t">${{esc(x.title)}}</div><div class="g">${{esc(x.hair)}} · ${{esc(x.tags.join('/'))}} · ${{esc(x.month)}}</div></div></div>`).join(''):'<div class="empty">没有匹配的图，清一下筛选试试～</div>';
}}
$('#grid').onclick=e=>{{const c=e.target.closest('.card');if(c)openLB(shown.findIndex(x=>x.n==c.dataset.n));}};
['#q','#fTag','#fHair','#fMonth'].forEach(s=>$(s).addEventListener('input',render));
function openLB(i){{if(i<0||i>=shown.length)return;cur=i;paint();$('#lb').classList.add('on');document.body.style.overflow='hidden';}}
function closeLB(){{$('#lb').classList.remove('on');document.body.style.overflow='';}}
function step(d){{cur=(cur+d+shown.length)%shown.length;paint();}}
function paint(){{const x=shown[cur];if(!x)return;
 $('#lbBig').src=x.src;$('#lbTitle').textContent=`R${{String(x.round).padStart(3,'0')}} · ${{x.title}} · ${{x.slot}}  (${{cur+1}}/${{shown.length}})`;
 $('#lbInfo').innerHTML=`<b>${{esc(x.outfit)}}</b> · ${{esc(x.hair)}} · ${{esc(x.tags.join(' / '))}} · ${{esc(x.month)}} · source=${{esc(x.source)}}`+
  (x.lines.length?`<br><b>这轮的话</b><br>${{x.lines.map(esc).join('<br>')}}`:'')+
  `<br><b>终稿 prompt</b><pre>${{esc(x.prompt)}}</pre>`;
 $('#lbInfo').scrollTop=0;}}
document.addEventListener('keydown',e=>{{if(!$('#lb').classList.contains('on'))return;if(e.key==='Escape')closeLB();if(e.key==='ArrowLeft')step(-1);if(e.key==='ArrowRight')step(1);}});
$('#themeBtn').onclick=()=>{{const d=document.documentElement;d.dataset.t=d.dataset.t==='light'?'':'light';}};
render();
</script></body></html>"""


def self_test():
    d = {"schema": 2, "rounds": [
        {"round": 1, "id": "20261126a_a", "title": "渡轮", "hair": "锁骨微卷",
         "tags": ["渡轮"], "month": "2026-11", "outfit_id": "SUM-0069", "source": "yuanbao",
         "base": "rounds/20261126a_a",
         "images": [{"file": f"{i:02d}_{v}.png", "view": v, "prompt": f"{i:02d}_{v}.md"}
                    for i, v in enumerate(["front", "side", "seat", "close"], 1)], "lines": ["一句话"]}]}
    items = [{"n": i, "src": "data:image/jpeg;base64,AAAA", "round": 1, "title": "渡轮", "id": "a",
              "slot": f"0{i}", "hair": "锁骨微卷", "tags": ["渡轮"], "month": "2026-11",
              "outfit": "SUM-0069", "source": "yuanbao", "prompt": "提示词", "lines": ["一句话"]}
             for i in range(1, 5)]
    h = render(items, d["rounds"])
    assert h.startswith("<!doctype html>") and "const DATA=" in h
    assert all(k in h for k in ("grid-template-columns:repeat(2,1fr)", "fHair", "fTag", "fMonth",
                                "openLB", "step(-1)", "data:image/jpeg;base64"))
    assert "</html>" in h
    print(f"self-test OK：离线单文件画廊结构齐全（{len(h)} 字符模板）")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="archive_repo", help="本地镜像根目录")
    ap.add_argument("--out", default="唐唐终稿图鉴.html", help="输出单文件 HTML")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test(); return
    items, meta = collect(a.root)
    out = Path(a.out)
    out.write_text(render(items, meta), encoding="utf-8")
    print(f"已生成 {out.resolve()} | {len(meta)} 轮 {len(items)} 张图 | {out.stat().st_size/1024/1024:.2f} MiB | 完全离线")


if __name__ == "__main__":
    main()
