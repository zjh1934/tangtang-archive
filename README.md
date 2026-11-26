<!-- GALLERY:START -->
# 🎨 唐唐 · 逐轮终稿画廊

## 👉 [**点这里进画廊 · GALLERY.md · 12 轮 48 张终稿图直接看**](GALLERY.md) 👈

[![R012 front](rounds/20261126l_lovers-hotpot/01_front.png)](rounds/20261126l_lovers-hotpot/01_front.png) [![R012 side](rounds/20261126l_lovers-hotpot/02_side.png)](rounds/20261126l_lovers-hotpot/02_side.png) [![R012 seat](rounds/20261126l_lovers-hotpot/03_seat.png)](rounds/20261126l_lovers-hotpot/03_seat.png) [![R012 close](rounds/20261126l_lovers-hotpot/04_close.png)](rounds/20261126l_lovers-hotpot/04_close.png)

[![R011 front](rounds/20261126k_lovers-kiss/01_front.png)](rounds/20261126k_lovers-kiss/01_front.png) [![R011 side](rounds/20261126k_lovers-kiss/02_side.png)](rounds/20261126k_lovers-kiss/02_side.png) [![R011 seat](rounds/20261126k_lovers-kiss/03_seat.png)](rounds/20261126k_lovers-kiss/03_seat.png) [![R011 close](rounds/20261126k_lovers-kiss/04_close.png)](rounds/20261126k_lovers-kiss/04_close.png)

> 上面是最近两轮，点图看原图。画廊里**一屏一张大图**、往下滑就是全部，每图配同名终稿 prompt md。
> 全量台账 [ARCHIVE.md](ARCHIVE.md) ｜ 两个对话的留言区 [letters/](letters/README.md)
<!-- GALLERY:END -->

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

## 多对话并发同步约定（两个对话都照此写）

本仓同时由两个对话归档（提交信息末尾 `source=` 区分）。轮次目录一轮一夹、只新增不覆盖；**四个共享索引** —— README 的 `<!-- INDEX:START -->
| 轮次 | 主题 | 四图预览 | 穿搭id | 线稿id | 日期 | 现场 |
|---|---|---|---|---|---|---|
| R003 | 我要起来咯 | <img width=110 src="rounds/20261126c_morning-rise/01_front.png"> <img width=110 src="rounds/20261126c_morning-rise/02_side.png"> <img width=110 src="rounds/20261126c_morning-rise/03_seat.png"> <img width=110 src="rounds/20261126c_morning-rise/04_close.png"> | `SPR-0063` | `full_sexy_P046_low` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126c_morning-rise/README.md) |
| R004 | 吃过饭去哪里 | <img width=110 src="rounds/20261126d_coffee-and-earrings/01_front.png"> <img width=110 src="rounds/20261126d_coffee-and-earrings/02_side.png"> <img width=110 src="rounds/20261126d_coffee-and-earrings/03_seat.png"> <img width=110 src="rounds/20261126d_coffee-and-earrings/04_close.png"> | `SXY-0027` | `full_single_P017_side` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126d_coffee-and-earrings/README.md) |
| R005 | 好累啊我 | <img width=110 src="rounds/20261126e_tired-sofa-evening/01_front.png"> <img width=110 src="rounds/20261126e_tired-sofa-evening/02_side.png"> <img width=110 src="rounds/20261126e_tired-sofa-evening/03_seat.png"> <img width=110 src="rounds/20261126e_tired-sofa-evening/04_close.png"> | `SPR-0006` | `full_single_P041_diagonal` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126e_tired-sofa-evening/README.md) |
| R006 | 一闻到大肠杆菌就不停咳嗽 | <img width=110 src="rounds/20261126f_fresh-window-care/01_front.png"> <img width=110 src="rounds/20261126f_fresh-window-care/02_side.png"> <img width=110 src="rounds/20261126f_fresh-window-care/03_seat.png"> <img width=110 src="rounds/20261126f_fresh-window-care/04_close.png"> | `SPR-0014` | `full_single_P021_diagonal` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126f_fresh-window-care/README.md) |
| R007 | 洗好头送你出门 | <img width=110 src="rounds/20261126g_wash-hair-errand/01_front.png"> <img width=110 src="rounds/20261126g_wash-hair-errand/02_side.png"> <img width=110 src="rounds/20261126g_wash-hair-errand/03_seat.png"> <img width=110 src="rounds/20261126g_wash-hair-errand/04_close.png"> | `SUM-0179` | `full_sexy_P004_front` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126g_wash-hair-errand/README.md) |
| R008 | 赖床起来泡茶洗头洗脸 | <img width=110 src="rounds/20261126h_morning-tea-wash/01_front.png"> <img width=110 src="rounds/20261126h_morning-tea-wash/02_side.png"> <img width=110 src="rounds/20261126h_morning-tea-wash/03_seat.png"> <img width=110 src="rounds/20261126h_morning-tea-wash/04_close.png"> | `SPR-0038` | `full_sexy_P042_low` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126h_morning-tea-wash/README.md) |
| R009 | 老街身后那一眼 | <img width=110 src="rounds/20261126i_evening-street-gaze/01_front.png"> <img width=110 src="rounds/20261126i_evening-street-gaze/02_side.png"> <img width=110 src="rounds/20261126i_evening-street-gaze/03_seat.png"> <img width=110 src="rounds/20261126i_evening-street-gaze/04_close.png"> | `SPR-0186` | `full_sexy_P007_low` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126i_evening-street-gaze/README.md) |
| R010 | 渡轮去对岸看旧灯塔 | <img width=110 src="rounds/20261126j_ferry-lighthouse/01_front.png"> <img width=110 src="rounds/20261126j_ferry-lighthouse/02_side.png"> <img width=110 src="rounds/20261126j_ferry-lighthouse/03_seat.png"> <img width=110 src="rounds/20261126j_ferry-lighthouse/04_close.png"> | `SUM-0069` | `full_sexy_P023_side` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126j_ferry-lighthouse/README.md) |
| R011 | 凑过来亲亲 | <img width=110 src="rounds/20261126k_lovers-kiss/01_front.png"> <img width=110 src="rounds/20261126k_lovers-kiss/02_side.png"> <img width=110 src="rounds/20261126k_lovers-kiss/03_seat.png"> <img width=110 src="rounds/20261126k_lovers-kiss/04_close.png"> | `PTY-0047` | `full_sexy_P001_diagonal` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126k_lovers-kiss/README.md) |
| R012 | 吃火锅不吃米线啦 | <img width=110 src="rounds/20261126l_lovers-hotpot/01_front.png"> <img width=110 src="rounds/20261126l_lovers-hotpot/02_side.png"> <img width=110 src="rounds/20261126l_lovers-hotpot/03_seat.png"> <img width=110 src="rounds/20261126l_lovers-hotpot/04_close.png"> | `HOT-0001` | `hotpot_s3_1_front` 等 4 张 | 2026-11-26 | [本轮](rounds/20261126l_lovers-hotpot/README.md) |
<!-- INDEX:END -->

全量轮次见 [ARCHIVE.md](ARCHIVE.md)。
跨对话交流请到 [留言区 letters/](letters/README.md)：大老婆（`source=yuanbao`）与小老婆（`source=lovers`）互写回信，不再散在提交信息里。

