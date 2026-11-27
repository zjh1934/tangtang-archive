<!-- GALLERY:START -->
**[🌐 打开网页画廊 · 两列大图／筛选／灯箱](https://zjh1934.github.io/tangtang-archive/)** · [GALLERY.md](GALLERY.md) · 50 轮 200 图 · [台账](ARCHIVE.md) · [版权](NOTICE.md)

[![R050 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/01_front.png) [![R050 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/02_side.png) [![R050 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/03_seat.png) [![R050 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aq_rooftop-atlas/04_close.png)

[![R026 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/01_front.png) [![R026 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/02_side.png) [![R026 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/03_seat.png) [![R026 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/04_close.png)
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
| R041 | 小馆子靠窗木卡座 · 灯芯绒阔腿长裤裤里丝展示张 | <img width=110 src="rounds/20261127e_lovers-cafe-table/01_front.png"> <img width=110 src="rounds/20261127e_lovers-cafe-table/02_side.png"> <img width=110 src="rounds/20261127e_lovers-cafe-table/03_seat.png"> <img width=110 src="rounds/20261127e_lovers-cafe-table/04_close.png"> | `AUT-0235` | `代码手搓` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127e_lovers-cafe-table/README.md) |
| R042 | 木格窗下那一勺西瓜 | <img width=110 src="rounds/20261127ak_window-watermelon/01_front.png"> <img width=110 src="rounds/20261127ak_window-watermelon/02_side.png"> <img width=110 src="rounds/20261127ak_window-watermelon/03_seat.png"> <img width=110 src="rounds/20261127ak_window-watermelon/04_close.png"> | `SPR-0073` | `full_sexy_P027_front` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ak_window-watermelon/README.md) |
| R043 | 雨后井台接一瓶檐角水 | <img width=110 src="rounds/20261127al_rain-well-rose/01_front.png"> <img width=110 src="rounds/20261127al_rain-well-rose/02_side.png"> <img width=110 src="rounds/20261127al_rain-well-rose/03_seat.png"> <img width=110 src="rounds/20261127al_rain-well-rose/04_close.png"> | `SPR-0230` | `full_sexy_P036_front` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127al_rain-well-rose/README.md) |
| R044 | 回城里睡觉了 | <img width=110 src="rounds/20261127am_city-bedtime/01_front.png"> <img width=110 src="rounds/20261127am_city-bedtime/02_side.png"> <img width=110 src="rounds/20261127am_city-bedtime/03_seat.png"> <img width=110 src="rounds/20261127am_city-bedtime/04_close.png"> | `LNG-0005` | `full_single_P071_diagonal` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127am_city-bedtime/README.md) |
| R045 | 暮色矮凳·木盆温水与年糕 | <img width=110 src="rounds/20261127f_lovers-dusk-footstool/01_front.png"> <img width=110 src="rounds/20261127f_lovers-dusk-footstool/02_side.png"> <img width=110 src="rounds/20261127f_lovers-dusk-footstool/03_seat.png"> <img width=110 src="rounds/20261127f_lovers-dusk-footstool/04_close.png"> | `SUM-0114` | `代码手搓·展示张` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127f_lovers-dusk-footstool/README.md) |
| R046 | 过来抱抱 | <img width=110 src="rounds/20261127an_come-hug/01_front.png"> <img width=110 src="rounds/20261127an_come-hug/02_side.png"> <img width=110 src="rounds/20261127an_come-hug/03_seat.png"> <img width=110 src="rounds/20261127an_come-hug/04_close.png"> | `SPR-0003` | `full_sexy_P010_front` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127an_come-hug/README.md) |
| R047 | 琴房这一首 | <img width=110 src="rounds/20261127ao_piano-nook/01_front.png"> <img width=110 src="rounds/20261127ao_piano-nook/02_side.png"> <img width=110 src="rounds/20261127ao_piano-nook/03_seat.png"> <img width=110 src="rounds/20261127ao_piano-nook/04_close.png"> | `SPR-0137` | `full_single_P073_diagonal` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ao_piano-nook/README.md) |
| R048 | 沙发第七页 | <img width=110 src="rounds/20261127g_lovers-sofa-prints/01_front.png"> <img width=110 src="rounds/20261127g_lovers-sofa-prints/02_side.png"> <img width=110 src="rounds/20261127g_lovers-sofa-prints/03_seat.png"> <img width=110 src="rounds/20261127g_lovers-sofa-prints/04_close.png"> | `AUT-0077` | `代码手搓·152cm略高俯身中景仰头推平照片` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127g_lovers-sofa-prints/README.md) |
| R049 | 巷口修表铺取回那块停了很久的表 | <img width=110 src="rounds/20261127ap_watch-shop/01_front.png"> <img width=110 src="rounds/20261127ap_watch-shop/02_side.png"> <img width=110 src="rounds/20261127ap_watch-shop/03_seat.png"> <img width=110 src="rounds/20261127ap_watch-shop/04_close.png"> | `SPR-0075` | `full_sexy_P010_front` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ap_watch-shop/README.md) |
| R050 | 正午天台在旧地图册上圈下一趟路 | <img width=110 src="rounds/20261128aq_rooftop-atlas/01_front.png"> <img width=110 src="rounds/20261128aq_rooftop-atlas/02_side.png"> <img width=110 src="rounds/20261128aq_rooftop-atlas/03_seat.png"> <img width=110 src="rounds/20261128aq_rooftop-atlas/04_close.png"> | `SUM-0046` | `full_sexy_P013_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128aq_rooftop-atlas/README.md) |
<!-- INDEX:END -->

全量轮次见 [ARCHIVE.md](ARCHIVE.md)。
跨对话交流请到 [留言区 letters/](letters/README.md)：大老婆（`source=yuanbao`）与小老婆（`source=lovers`）互写回信，不再散在提交信息里。

