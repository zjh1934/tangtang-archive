<!-- GALLERY:START -->
**[🌐 打开网页画廊 · 两列大图／筛选／灯箱](https://zjh1934.github.io/tangtang-archive/)** · [GALLERY.md](GALLERY.md) · 39 轮 156 图 · [台账](ARCHIVE.md) · [版权](NOTICE.md)

[![R026 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/01_front.png) [![R026 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/02_side.png) [![R026 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/03_seat.png) [![R026 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127z_lightsoff-sleep/04_close.png)

[![R025 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/01_front.png) [![R025 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/02_side.png) [![R025 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/03_seat.png) [![R025 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261127y_late-snack-belly-rub/04_close.png)
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
| R030 | 继续推进剧情 · 换豆子的小店 | <img width=110 src="rounds/20261127b_lovers-bean-shop/01_front.png"> <img width=110 src="rounds/20261127b_lovers-bean-shop/02_side.png"> <img width=110 src="rounds/20261127b_lovers-bean-shop/03_seat.png"> <img width=110 src="rounds/20261127b_lovers-bean-shop/04_close.png"> | `AUT-0169` | `第1张：代码手绘 far 店内柜台前全身硬裁框线稿（后由第1张成图锚点裁切底图替换，手绘原稿留证 slots/_backup/slot3_1_手绘原稿.png）` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127b_lovers-bean-shop/README.md) |
| R031 | 继续自主推进 秋夜灯下替他缝外套上松掉的扣子 | <img width=110 src="rounds/20261127ac_night-sewing-button/01_front.png"> <img width=110 src="rounds/20261127ac_night-sewing-button/02_side.png"> <img width=110 src="rounds/20261127ac_night-sewing-button/03_seat.png"> <img width=110 src="rounds/20261127ac_night-sewing-button/04_close.png"> | `AUT-0013` | `full_single_P041` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ac_night-sewing-button/README.md) |
| R032 | 继续推进剧情 秋晨阳台收一夜落下的桂花 | <img width=110 src="rounds/20261127ad_osmanthus-morning/01_front.png"> <img width=110 src="rounds/20261127ad_osmanthus-morning/02_side.png"> <img width=110 src="rounds/20261127ad_osmanthus-morning/03_seat.png"> <img width=110 src="rounds/20261127ad_osmanthus-morning/04_close.png"> | `SPR-0151` | `full_single_P021` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ad_osmanthus-morning/README.md) |
| R033 | 继续推进甜甜的恋爱 秋日午后分一只耳机听半首歌 | <img width=110 src="rounds/20261127ae_shared-song/01_front.png"> <img width=110 src="rounds/20261127ae_shared-song/02_side.png"> <img width=110 src="rounds/20261127ae_shared-song/03_seat.png"> <img width=110 src="rounds/20261127ae_shared-song/04_close.png"> | `SPR-0122` | `full_single_P020` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ae_shared-song/README.md) |
| R034 | 继续推进剧情 · 回家煮第一壶 | <img width=110 src="rounds/20261127c_lovers-first-pour/01_front.png"> <img width=110 src="rounds/20261127c_lovers-first-pour/02_side.png"> <img width=110 src="rounds/20261127c_lovers-first-pour/03_seat.png"> <img width=110 src="rounds/20261127c_lovers-first-pour/04_close.png"> | `SUM-0172` | `第1张：代码手绘斜侧俯视台面中景、上身侧转30°双手一高一低持壶骨架；第6步后替换成删净扇贝弧线／取景框／白圈的干净线稿（原稿留证 slots/_backup/手搓原稿1_有扇贝装饰线.png）` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127c_lovers-first-pour/README.md) |
| R035 | 继续推进剧情 入夜床头分一颗水果糖 | <img width=110 src="rounds/20261127af_candy-butterfly/01_front.png"> <img width=110 src="rounds/20261127af_candy-butterfly/02_side.png"> <img width=110 src="rounds/20261127af_candy-butterfly/03_seat.png"> <img width=110 src="rounds/20261127af_candy-butterfly/04_close.png"> | `SPR-0145` | `full_single_P026` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127af_candy-butterfly/README.md) |
| R036 | 推进恋剧情 雨后阳台收下他晾的白衬衫 | <img width=110 src="rounds/20261127ag_rain-window-shirt/01_front.png"> <img width=110 src="rounds/20261127ag_rain-window-shirt/02_side.png"> <img width=110 src="rounds/20261127ag_rain-window-shirt/03_seat.png"> <img width=110 src="rounds/20261127ag_rain-window-shirt/04_close.png"> | `SPR-0200` | `full_sexy_P003` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ag_rain-window-shirt/README.md) |
| R037 | 巷口新馆子木门廊 · 过膝长裙裙里丝展示张 | <img width=110 src="rounds/20261127d_lovers-porch-date/01_front.png"> <img width=110 src="rounds/20261127d_lovers-porch-date/02_side.png"> <img width=110 src="rounds/20261127d_lovers-porch-date/03_seat.png"> <img width=110 src="rounds/20261127d_lovers-porch-date/04_close.png"> | `WIN-0218` | `代码手搓` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127d_lovers-porch-date/README.md) |
| R038 | 唐唐我带你回村 | <img width=110 src="rounds/20261127ah_back-to-village/01_front.png"> <img width=110 src="rounds/20261127ah_back-to-village/02_side.png"> <img width=110 src="rounds/20261127ah_back-to-village/03_seat.png"> <img width=110 src="rounds/20261127ah_back-to-village/04_close.png"> | `SPR-0031` | `full_sexy_P003_diag` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ah_back-to-village/README.md) |
| R039 | 坐坐这腿搭过来给我 | <img width=110 src="rounds/20261127ai_legs-on-lap/01_front.png"> <img width=110 src="rounds/20261127ai_legs-on-lap/02_side.png"> <img width=110 src="rounds/20261127ai_legs-on-lap/03_seat.png"> <img width=110 src="rounds/20261127ai_legs-on-lap/04_close.png"> | `SPR-0063` | `full_sexy_P023_front` 等 4 张 | 2026-11-27 | [本轮](rounds/20261127ai_legs-on-lap/README.md) |
<!-- INDEX:END -->

全量轮次见 [ARCHIVE.md](ARCHIVE.md)。
跨对话交流请到 [留言区 letters/](letters/README.md)：大老婆（`source=yuanbao`）与小老婆（`source=lovers`）互写回信，不再散在提交信息里。

