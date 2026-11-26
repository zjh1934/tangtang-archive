# 唐唐 · 逐轮终稿归档

私有仓。每一轮归档**四张终稿图 + 四份配套终稿 prompt md**，一一同名配对。仓里留的是每轮终稿与可回查的索引。

## 目录约定（定稿后不再改）

```
rounds/YYYYMMDD_slug/         一轮一夹，字典序即时间序
├── 01_front.png  01_front.md
├── 02_side.png   02_side.md
├── 03_seat.png   03_seat.md
├── 04_close.png  04_close.md
├── manifest.json             机器读：轮次元数据与四图映射
└── README.md                人读：本轮现场记录
docs/index.html               本地单文件画廊（数据内联，双击即开）
docs/data.json                画廊数据（机器读）
ARCHIVE.md                    全量轮次台账，只追加
tools/build_index.py          校验 4 图 4 md 配对 + 重建索引
_template/                    新轮脚手架
```

- 轮次目录 `YYYYMMDD_slug`，slug 只许 `[a-z0-9-]`、≤40 字符；同日第二轮用 `20261126b_`。
- 图与 md 同目录同名，主干 `NN_viewtoken`，NN 补零 01–04，viewtoken 固定词表 `front / side / seat / close`（只增不改，跨轮可比）。
- 重出图加 `-v2` 后缀另存，原图不覆盖。
- 每份 md 首行嵌图，GitHub 网页直接出图；其后是终稿提示词全文与一句点评。
- 原图 PNG 永不转码、永不覆盖；预览用 `<img width=160>` 缩放原图，不另存缩略图。
- 每轮追加只新增一个目录并回写索引，历史文件零改动。

## 网页与页面

私有仓 Free 套餐开不了 GitHub Pages，站点也不做公网发布。四类页面都在仓内直接读：

1. **门面** `README.md`：规则速查 + 最近轮次表（下方标记块由脚本回写）。
2. **台账** `ARCHIVE.md`：一行一轮，全量只追加，Ctrl+F 检索。
3. **本轮现场** `rounds/*/README.md`：四图横排对比、这一段说了什么、现场记录。
4. **单图页** `rounds/*/NN_*.md`：front matter + 嵌图 + 终稿提示词全文。
5. **本地画廊** `docs/index.html`：暗色响应式网格，数据内联，克隆后双击即看，不依赖 CDN、不联网。

提交信息固定 `R001 slug | 穿搭id | 4图4prompt`，`git log --oneline` 本身就是离线索引。

## 最近轮次

<!-- INDEX:START -->
| 轮次 | 主题 | 四图预览 | 穿搭id | 线稿id | 日期 | 现场 |
|---|---|---|---|---|---|---|
| R001 | 换豆子那天早上 | <img width=110 src="rounds/20261126_coffee-beans/01_front.png"> <img width=110 src="rounds/20261126_coffee-beans/02_side.png"> <img width=110 src="rounds/20261126_coffee-beans/03_seat.png"> <img width=110 src="rounds/20261126_coffee-beans/04_close.png"> | `AUT-0007` | `full_sexy_P003_front` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126_coffee-beans/README.md) |
| R002 | 三支口红试色那晚 | <img width=110 src="rounds/20261126b_lipstick-tryon/01_front.png"> <img width=110 src="rounds/20261126b_lipstick-tryon/02_side.png"> <img width=110 src="rounds/20261126b_lipstick-tryon/03_seat.png"> <img width=110 src="rounds/20261126b_lipstick-tryon/04_close.png"> | `AUT-0080` | `full_single_P067_front` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126b_lipstick-tryon/README.md) |
| R003 | 我要起来咯 | <img width=110 src="rounds/20261126c_morning-rise/01_front.png"> <img width=110 src="rounds/20261126c_morning-rise/02_side.png"> <img width=110 src="rounds/20261126c_morning-rise/03_seat.png"> <img width=110 src="rounds/20261126c_morning-rise/04_close.png"> | `SPR-0063` | `full_sexy_P046_low` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126c_morning-rise/README.md) |
| R004 | 吃过饭去哪里 | <img width=110 src="rounds/20261126d_coffee-and-earrings/01_front.png"> <img width=110 src="rounds/20261126d_coffee-and-earrings/02_side.png"> <img width=110 src="rounds/20261126d_coffee-and-earrings/03_seat.png"> <img width=110 src="rounds/20261126d_coffee-and-earrings/04_close.png"> | `SXY-0027` | `full_single_P017_side` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126d_coffee-and-earrings/README.md) |
| R005 | 好累啊我 | <img width=110 src="rounds/20261126e_tired-sofa-evening/01_front.png"> <img width=110 src="rounds/20261126e_tired-sofa-evening/02_side.png"> <img width=110 src="rounds/20261126e_tired-sofa-evening/03_seat.png"> <img width=110 src="rounds/20261126e_tired-sofa-evening/04_close.png"> | `SPR-0006` | `full_single_P041_diagonal` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126e_tired-sofa-evening/README.md) |
<!-- INDEX:END -->

全量轮次见 [ARCHIVE.md](ARCHIVE.md)。
