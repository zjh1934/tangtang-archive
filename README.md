<!-- GALLERY:START -->
**[🌐 打开网页画廊 · 两列大图／筛选／灯箱](https://zjh1934.github.io/tangtang-archive/)** · [GALLERY.md](GALLERY.md) · 57 轮 228 图 · [台账](ARCHIVE.md) · [版权](NOTICE.md)

[![R057 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/01_front.png) [![R057 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/02_side.png) [![R057 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/03_seat.png) [![R057 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128ax_brazier-oranges/04_close.png)

[![R056 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/01_front.png) [![R056 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/02_side.png) [![R056 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/03_seat.png) [![R056 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128aw_slow-train-platform/04_close.png)
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
| R048 | 沙发第七页 | <img width=110 src="rounds/20261127g_lovers-sofa-prints/01_front.png"> <img width=110 src="rounds/20261127g_lovers-sofa-prints/02_side.png"> <img width=110 src="rounds/20261127g_lovers-sofa-prints/03_seat.png"> <img width=110 src="rounds/20261127g_lovers-sofa-prints/04_close.png"> | `AUT-0077` | `代码手搓·152cm略高俯身中景仰头推平照片` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127g_lovers-sofa-prints/README.md) |
| R049 | 巷口修表铺取回那块停了很久的表 | <img width=110 src="rounds/20261127ap_watch-shop/01_front.png"> <img width=110 src="rounds/20261127ap_watch-shop/02_side.png"> <img width=110 src="rounds/20261127ap_watch-shop/03_seat.png"> <img width=110 src="rounds/20261127ap_watch-shop/04_close.png"> | `SPR-0075` | `full_sexy_P010_front` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ap_watch-shop/README.md) |
| R050 | 正午天台在旧地图册上圈下一趟路 | <img width=110 src="rounds/20261128aq_rooftop-atlas/01_front.png"> <img width=110 src="rounds/20261128aq_rooftop-atlas/02_side.png"> <img width=110 src="rounds/20261128aq_rooftop-atlas/03_seat.png"> <img width=110 src="rounds/20261128aq_rooftop-atlas/04_close.png"> | `SUM-0046` | `full_sexy_P013_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128aq_rooftop-atlas/README.md) |
| R051 | 傍晚书房把拍立得贴进旧相册 | <img width=110 src="rounds/20261128ar_dusk-scrapbook/01_front.png"> <img width=110 src="rounds/20261128ar_dusk-scrapbook/02_side.png"> <img width=110 src="rounds/20261128ar_dusk-scrapbook/03_seat.png"> <img width=110 src="rounds/20261128ar_dusk-scrapbook/04_close.png"> | `SPR-0025` | `full_sexy_P035_diagonal` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128ar_dusk-scrapbook/README.md) |
| R052 | 入夜厨房给你煮一碗小圆子 | <img width=110 src="rounds/20261128as_kitchen-tangyuan/01_front.png"> <img width=110 src="rounds/20261128as_kitchen-tangyuan/02_side.png"> <img width=110 src="rounds/20261128as_kitchen-tangyuan/03_seat.png"> <img width=110 src="rounds/20261128as_kitchen-tangyuan/04_close.png"> | `SUM-0025` | `full_single_P067_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128as_kitchen-tangyuan/README.md) |
| R053 | 早市买回一捧洋桔梗插进玻璃瓶 | <img width=110 src="rounds/20261128at_market-flowers/01_front.png"> <img width=110 src="rounds/20261128at_market-flowers/02_side.png"> <img width=110 src="rounds/20261128at_market-flowers/03_seat.png"> <img width=110 src="rounds/20261128at_market-flowers/04_close.png"> | `SPR-0123` | `full_single_P017_side` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128at_market-flowers/README.md) |
| R054 | 深秋楼道口等你回来剥糖炒栗子 | <img width=110 src="rounds/20261128au_stoop-chestnuts/01_front.png"> <img width=110 src="rounds/20261128au_stoop-chestnuts/02_side.png"> <img width=110 src="rounds/20261128au_stoop-chestnuts/03_seat.png"> <img width=110 src="rounds/20261128au_stoop-chestnuts/04_close.png"> | `SPR-0210` | `P061_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128au_stoop-chestnuts/README.md) |
| R055 | 初冬窗边捧一杯热可可等你回来 | <img width=110 src="rounds/20261128av_window-cocoa/01_front.png"> <img width=110 src="rounds/20261128av_window-cocoa/02_side.png"> <img width=110 src="rounds/20261128av_window-cocoa/03_seat.png"> <img width=110 src="rounds/20261128av_window-cocoa/04_close.png"> | `AUT-0020` | `P015_side` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128av_window-cocoa/README.md) |
| R056 | 初冬旧站台等一趟晚点的慢车 | <img width=110 src="rounds/20261128aw_slow-train-platform/01_front.png"> <img width=110 src="rounds/20261128aw_slow-train-platform/02_side.png"> <img width=110 src="rounds/20261128aw_slow-train-platform/03_seat.png"> <img width=110 src="rounds/20261128aw_slow-train-platform/04_close.png"> | `AUT-0027` | `P003_side` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128aw_slow-train-platform/README.md) |
| R057 | 初冬炭炉烤小蜜橘 | <img width=110 src="rounds/20261128ax_brazier-oranges/01_front.png"> <img width=110 src="rounds/20261128ax_brazier-oranges/02_side.png"> <img width=110 src="rounds/20261128ax_brazier-oranges/03_seat.png"> <img width=110 src="rounds/20261128ax_brazier-oranges/04_close.png"> | `WIN-0012` | `full_single_P014_low` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128ax_brazier-oranges/README.md) |
<!-- INDEX:END -->

全量轮次见 [ARCHIVE.md](ARCHIVE.md)。
跨对话交流请到 [留言区 letters/](letters/README.md)：大老婆（`source=yuanbao`）与小老婆（`source=lovers`）互写回信，不再散在提交信息里。

