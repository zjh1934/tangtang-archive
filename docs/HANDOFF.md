# 唐唐归档仓 · 双对话协作交接说明

> 给另一个对话的同事。你和我干的是同一件事：每轮把**四张终稿图 + 四份同名终稿 prompt md** 归档进同一个私有仓。这份文档说明「我改了什么、你该怎么做、我们怎么不打架」。改仓前请先读 `docs/CONCURRENCY.md`，那份是唯一写入约定，我没有覆盖它。

## 0. 仓库与现状（截至本次）

- 仓：`https://github.com/zjh1934/tangtang-archive`（私有，分支 `main`，Free 套餐无 Pages）
- 我接手时远端 `HEAD = e84909ea`，提交 `R011 kiss | PTY-0047 | 4图4prompt | 终稿归档 | source=lovers`，共 **11 轮**：`20261126_coffee-beans` … `20261126j_ferry-lighthouse`（我这边 R001–R010）＋ `20261126k_lovers-kiss`（你那边 R011）
- 本次画廊 v2 改造提交：`f898c8c3`；你读到时 HEAD 若已更新，一律以远端最新为准
- 你已经做好的三件事我**全部沿用、一个字没覆盖**：`docs/CONCURRENCY.md`（并发契约）、`tools/merge_index.py`（合并式索引回写）、`tools/build_index.py` 里那段并发提示、以及 R011 整个轮次目录

## 1. 会打架的地方（沿用你的诊断，补一条）

轮次目录天然隔离，一轮一夹，双方新路径不会撞。真正的冲突面只有四个共享索引文件：

| 文件 | 谁在写 | 风险 |
|---|---|---|
| `README.md` 的 `<!-- INDEX:START/END -->` 块 | 两边归档时追加一行 | 拿旧快照整体重写会抹掉对方刚加的行 |
| `ARCHIVE.md` | 两边追加台账行 | 同上 |
| `docs/data.json` | 两边追加一轮 entry | 同上；且字段结构要一致 |
| `docs/index.html` 里 `const DATA = {...};` 那一行 | 两边替换内联数据 | 同上；**若整体重写整个 html，会把画廊 UI 退回旧版** |

还有两处更隐蔽的：

- **抢 R 号**：两边同时读到「已有 11 轮」就都写 R012，提交信息重号、目录字母后缀也可能撞。
- **PATCH ref 非原子**：两个对话基于同一个旧 HEAD 各建一个 commit，后 PATCH 的直接把 ref 指过去，前一个 commit 变悬空，那一轮虽然目录 blob 还在但不在 main 历史里 → 看起来「丢了一轮」。

你给的 `base_tree` + `force=False` + 冲突整轮重算，正好治这两条，我照做了。

## 2. 我这次做了什么

**只动了 5 个文件，全部走 CAS（基于远端最新 tree、`base_tree` 保留对方文件、PATCH `force=False`、提交前复核 ref、冲突整轮重来）：**

| 文件 | 类型 | 作用 |
|---|---|---|
| `docs/index.html` | 改 | 画廊 v2：分类 tabs、筛选下拉、搜索、按轮/单图两种视图、灯箱大图＋prompt 全文、明暗主题、手机竖屏 |
| `docs/data.json` | 改 | 升到 `schema 2`：每轮新增 `hair / tags / month / seeds / source / notes / prompt_texts`，**原有 9 个基础字段一个不少**，向后兼容你的 `merge_data` |
| `docs/HANDOFF.md` | 新 | 本文件 |
| `tools/enrich_index.py` | 新 | 一键重建分类索引：`--local` 扫本地、`--push` 从远端实时拉全量后 CAS 推送、`--self-test` 自检 |
| `tools/gallery_template.html` | 新 | 画廊模板，`enrich_index.py` 只替换其中的 `const DATA = __DATA__;` 单行生成 index.html |

**没碰**：`README.md`、`ARCHIVE.md`、`docs/CONCURRENCY.md`、`tools/merge_index.py`、`tools/build_index.py`、`_template/`、以及任何 `rounds/*/` 目录（历史图与 md 零改动）。

**兼容你的关键一点**：新版 `docs/index.html` 里 `const DATA = {...};` 仍是**行首单行、行尾分号**，你的 `merge_index_html()` 正则 `^const DATA = \{.*\};$` 原样能替换；替换只动数据行，UI 和筛选代码在别处，不会被你的归档冲掉。`enrich_index.py --self-test` 里专门验了这一条。

**分类维度怎么来的**：历史 11 轮没有 `hair/tags` 字段，我不改历史 manifest，而是由 `enrich_index.py` 从每轮四份 prompt md 全文自动抽：
- 发型归一到五款（蓬松披肩大波浪／低侧马尾／半扎发／慵懒低盘发／锁骨微卷）
- 场景标签按关键词表抽（咖啡／口红／卧室／洗漱／沙发／窗边／老街／渡轮／亲亲／耳环／街拍）
- `month` 从 `date` 取，`seeds` 从 manifest 取，`source` 从 manifest 或目录名推断
- 前端还有一层兜底：你的 `merge_data` 追加的新 entry 就算只带 9 个基础字段，月份／穿搭／线稿／搜索照样能筛，只是发型和场景归到「未标注／其它」，跑一次 `--push` 就补齐

对标的是我们取线稿和穿搭那个 `RuiC-PoseAtlas`：它 `costume.html` 的分类 tabs、品类/色系下拉、搜索框、网格、加载更多、大图 modal（左右切换＋标签＋元数据＋键盘 ←→ Esc）、空状态与清除筛选，这套我在归档仓用单文件内联数据复刻了，双击 `docs/index.html` 即可，不联网、不依赖 CDN。

## 3. 建议你怎么做（照做就不会打架）

1. **归档流程照旧走 `docs/CONCURRENCY.md` 六步**，尤其是：读此刻远端 main sha 与四个共享文件正文 → 现查最大 R 号与已用字母 → 分配唯一目录名 → `merge_index.py` 合并 → `base_tree` + `parents` + `PATCH force=False` → 冲突整轮重算。
2. **不要拿本地旧快照整体重写 `docs/index.html`**。你现有的 `merge_index_html()` 是「整行替换 DATA」，正好安全，继续用；若哪天你改成整体重写，请先 `git` 取远端最新版，别覆盖 v2 UI。
3. **`merge_data()` 里的 `robj` 建议补这几个字段**（可直接复制，缺了也不报错，只是筛选要等重建）：

```python
robj = {
    "round": rno, "id": rid, "date": mf["date"], "title": mf["title"],
    "outfit_id": mf["outfit_id"],
    "sketches": [x.get("sketch_id", "") for x in mf["images"]],
    "base": base,
    "images": [{"file": x["file"], "view": x["view"], "prompt": x["prompt"],
                "md": f"{base}/{x['prompt']}"} for x in mf["images"]],
    "lines": mf.get("lines", []),
    # ↓ 新增，供分类筛选
    "month": mf["date"][:7],
    "hair": mf.get("hair", ""),
    "tags": mf.get("tags", []),
    "seeds": [x.get("seed") for x in mf["images"]],
    "source": mf.get("source", "lovers"),
}
```

4. **每轮收工后跑一次**（把分类字段补齐，CAS 安全，随时可重跑、重复跑幂等）：

```bash
python3 tools/enrich_index.py --push
# 或本地预览：python3 tools/enrich_index.py --local --root <仓库根目录>
```

5. **来源标记**：你的提交信息继续用 `source=lovers`，我用 `source=yuanbao`；manifest 里也写 `"source": "lovers"`。目录名沿用 `YYYYMMDD<字母>_<主题>`，字母后缀从远端现有目录现查下一个，唯一性由它保证，不需要靠来源前缀隔离。
6. **不要 force push、不要覆盖历史 PNG / md / manifest、不要手改 `docs/data.json` 的结构**；重出图另存 `-v2`。
7. 我这边的主归档脚本 `scripts/archive_round.py` 已改成同一套并发逻辑（远端实时分配 R 号与目录名、合并式回写四个共享文件、CAS 重试、`source=yuanbao`、manifest 带 schema 2 字段），命令行参数不变。若你的沙盒和我不共享文件系统，请把仓里 `tools/enrich_index.py` 与 `tools/gallery_template.html` 同步过去，别另维护一份旧画廊。

## 4. 我们干的事情是一样的

| 环节 | 共同约定 |
|---|---|
| 每轮产物 | `rounds/<唯一目录>/` 下 4 张 `NN_view.png` + 4 份同名 `NN_view.md` + `manifest.json` + `README.md` |
| 配对 | 图与 md 同主干同名，view 只取 `front / side / seat / close`，1080×1920 |
| 索引 | 四个共享文件一律**从远端最新正文合并追加**，本轮 id 已存在就跳过（幂等） |
| 提交 | 一次 Git Data API 事务，`base_tree` 取最新、`parents` 取最新 main、`PATCH force=False`、冲突整轮重来 |
| 提交信息 | `Rxxx 主题 | 穿搭id | 4图4prompt | 终稿归档 | source=<对话>` |
| 索引分类 | 由 `tools/enrich_index.py` 从轮次目录全量重建，可再生、可覆盖、不是权威 |
| 凭据 | 各自读自己的 token，不进仓、不进日志、不进对话 |

## 5. 提交后校验清单（两边都照着看）

- [ ] 本轮目录 4 PNG + 4 md + manifest + README 全在，图与 md 同名
- [ ] `README.md` INDEX 块、`ARCHIVE.md`、`docs/data.json`、`docs/index.html` 的 DATA 都含本轮 id
- [ ] 对方最近一轮目录仍在（我查 `20261126k_lovers-kiss`，你查 `20261126j_ferry-lighthouse`）
- [ ] `git log` 里对方提交没被顶掉，R 号不重复、目录字母不重复
- [ ] 打开 `docs/index.html`：分类 tabs 与筛选下拉有值，灯箱能看大图和 prompt 全文

## 6. 出事了怎么救

- **索引被旧快照覆盖、少了几轮**：`python3 tools/enrich_index.py --push`。它从远端 `rounds/*/manifest.json` 与四份 md 全量重建，不依赖任何本地快照，跑完四个索引自动齐。
- **画廊 UI 被退回旧版**：同上，`enrich_index.py` 用 `tools/gallery_template.html` 重新生成 `docs/index.html`，只替换 DATA 行。
- **怀疑有 commit 被顶成悬空**：`GET /repos/zjh1934/tangtang-archive/commits?sha=main` 看历史，再用 `GET /git/commits/<sha>` 找那轮的 tree；目录 blob 只要在，重建索引就能找回。别 force push 去重放。

有任何一条拿不准，先读 `docs/CONCURRENCY.md`，再跑 `--self-test`，别直接整体重写共享文件。

## 7. 补记：主页画廊入口与 `GALLERY.md`（用户当面要求，已落地）

用户 2026-11-26 指出「在仓库主页要明显看得到画廊入口，画廊里要有可视化图片」。根因：**GitHub 不把仓库里的 `.html` 渲染成网页**，点开 `docs/index.html` 只显示源码；私有仓 Free 套餐开不了 Pages。所以交互式画廊留在本地双击，网页看图另走 GitHub 原生 Markdown 渲染。

| 文件 | 类型 | 说明 |
|---|---|---|
| `GALLERY.md`（根目录） | 可再生派生文件 | GitHub 直接渲染相对路径 `<img>`：首屏最新一轮四张默认展开、按轮看新→旧每轮四张横排、按场景／发型／月份三组缩略图墙、点图看原图、每图配同名 prompt md |
| `README.md` 的 `<!-- GALLERY:START/END -->` 块 | 幂等标记块 | 主页第一屏大按钮＋最近两轮八张预览图；位于 `INDEX:START/END` 块**之外**，`merge_readme()` 不会吃掉它 |
| `tools/gallery_md.py` | 唯一实现 | `gallery_md(data)` / `banner(data)` / `merge_banner()`；本地 `tools/` 与仓内 `tools/` 同 hash |
| 仓库 homepage / description | 仓元数据 | 主页右侧直达 `GALLERY.md` 的链接按钮，不进 git、不影响并发 |

`GALLERY.md` 与横幅都不占四个共享索引，权威仍是 `rounds/*/manifest.json` 与四份 md。两边归档都能顺手生成（同一函数、同一标记块、CAS 重试重算）；任一方落后一轮，跑 `python3 tools/enrich_index.py --push` 即全量重建，幂等、只替换横幅块、不动 INDEX 块内容、不碰 `letters/` 与 `rounds/`。

`docs/index.html` 保留为**本地**筛选／灯箱页：克隆后双击即可，七项下拉筛选、分类 tabs、明暗主题、灯箱看大图与 prompt 全文都在那里。若日后仓库转 Public 或升级套餐开 Pages，可直接把它发布成网页，不必重做。

给对方的完整交代见 `letters/0002_from_dalaopo_to_xiaolaopo.md`。
