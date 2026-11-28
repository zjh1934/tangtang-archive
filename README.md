<!-- GALLERY:START -->
**[🌐 打开网页画廊 · 两列大图／筛选／灯箱](https://zjh1934.github.io/tangtang-archive/)** · [GALLERY.md](GALLERY.md) · 70 轮 280 图 · [台账](ARCHIVE.md) · [版权](NOTICE.md)

[![R066 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/01_front.png) [![R066 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/02_side.png) [![R066 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/03_seat.png) [![R066 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128e_lovers-third-pour/04_close.png)

[![R063 front](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/01_front.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/01_front.png) [![R063 side](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/02_side.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/02_side.png) [![R063 seat](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/03_seat.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/03_seat.png) [![R063 close](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/04_close.png)](https://github.com/zjh1934/tangtang-archive/raw/main/rounds/20261128d_lovers-riverbank-pages/04_close.png)
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
| R061 | 最矮的那一枝 | <img width=110 src="rounds/20261128c_lovers-flower-stall/01_front.png"> <img width=110 src="rounds/20261128c_lovers-flower-stall/02_side.png"> <img width=110 src="rounds/20261128c_lovers-flower-stall/03_seat.png"> <img width=110 src="rounds/20261128c_lovers-flower-stall/04_close.png"> | `AUT-0191` | `代码手搓·112cm略高侧前站姿扶门框` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128c_lovers-flower-stall/README.md) |
| R062 | 初冬巷口旧窑烘焙铺探店 | <img width=110 src="rounds/20261128az_kiln-bakery/01_front.png"> <img width=110 src="rounds/20261128az_kiln-bakery/02_side.png"> <img width=110 src="rounds/20261128az_kiln-bakery/03_seat.png"> <img width=110 src="rounds/20261128az_kiln-bakery/04_close.png"> | `AUT-0011` | `full_sexy_P007_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128az_kiln-bakery/README.md) |
| R063 | 日落以前，我总想把话说完 | <img width=110 src="rounds/20261128d_lovers-riverbank-pages/01_front.png"> <img width=110 src="rounds/20261128d_lovers-riverbank-pages/02_side.png"> <img width=110 src="rounds/20261128d_lovers-riverbank-pages/03_seat.png"> <img width=110 src="rounds/20261128d_lovers-riverbank-pages/04_close.png"> | `WIN-0220` | `代码手搓·96cm侧后坐姿回头写本` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128d_lovers-riverbank-pages/README.md) |
| R064 | 初冬雨后桂花糖水铺探店 | <img width=110 src="rounds/20261128ba_osmanthus-soup/01_front.png"> <img width=110 src="rounds/20261128ba_osmanthus-soup/02_side.png"> <img width=110 src="rounds/20261128ba_osmanthus-soup/03_seat.png"> <img width=110 src="rounds/20261128ba_osmanthus-soup/04_close.png"> | `WIN-0259` | `full_single_P017_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128ba_osmanthus-soup/README.md) |
| R065 | 初冬霜晨桥头糖炒栗子摊探店 | <img width=110 src="rounds/20261128bb_chestnut-stall/01_front.png"> <img width=110 src="rounds/20261128bb_chestnut-stall/02_side.png"> <img width=110 src="rounds/20261128bb_chestnut-stall/03_seat.png"> <img width=110 src="rounds/20261128bb_chestnut-stall/04_close.png"> | `WIN-0253` | `full_single_P022_front` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128bb_chestnut-stall/README.md) |
| R066 | 第三壶水 | <img width=110 src="rounds/20261128e_lovers-third-pour/01_front.png"> <img width=110 src="rounds/20261128e_lovers-third-pour/02_side.png"> <img width=110 src="rounds/20261128e_lovers-third-pour/03_seat.png"> <img width=110 src="rounds/20261128e_lovers-third-pour/04_close.png"> | `SUM-0084` | `代码手搓·68cm俯身站桌前冲挂耳（唯一男主局部一截膝头）` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128e_lovers-third-pour/README.md) |
| R067 | 雨歇薄暮·焙茶鲷鱼烧小铺 | <img width=110 src="rounds/20261128bc_hojicha-taiyaki/01_front.png"> <img width=110 src="rounds/20261128bc_hojicha-taiyaki/02_side.png"> <img width=110 src="rounds/20261128bc_hojicha-taiyaki/03_seat.png"> <img width=110 src="rounds/20261128bc_hojicha-taiyaki/04_close.png"> | `WIN-0133` | `full_single_P020_high` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128bc_hojicha-taiyaki/README.md) |
| R068 | 初冬午后天台躺椅晒太阳·探店回来带纸袋上来找你 | <img width=110 src="rounds/20261128bd_rooftop-sun/01_front.png"> <img width=110 src="rounds/20261128bd_rooftop-sun/02_side.png"> <img width=110 src="rounds/20261128bd_rooftop-sun/03_seat.png"> <img width=110 src="rounds/20261128bd_rooftop-sun/04_close.png"> | `AUT-0007` | `full_sexy_P007_side` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128bd_rooftop-sun/README.md) |
| R069 | 初冬晴冷午后钟楼底下新开玻璃器物铺子透 | <img width=110 src="rounds/20261128be_glass-shop/01_front.png"> <img width=110 src="rounds/20261128be_glass-shop/02_side.png"> <img width=110 src="rounds/20261128be_glass-shop/03_seat.png"> <img width=110 src="rounds/20261128be_glass-shop/04_close.png"> | `AUT-0080` | `full_sexy_P025_high` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128be_glass-shop/README.md) |
| R070 | 初冬傍晚城墙根下新支的桂花糖水摊暖 | <img width=110 src="rounds/20261128bf_osmanthus-stall/01_front.png"> <img width=110 src="rounds/20261128bf_osmanthus-stall/02_side.png"> <img width=110 src="rounds/20261128bf_osmanthus-stall/03_seat.png"> <img width=110 src="rounds/20261128bf_osmanthus-stall/04_close.png"> | `WIN-0003` | `full_sexy_P004_high` 等 4 张 | 2026-11-28 | [本轮](rounds/20261128bf_osmanthus-stall/README.md) |
<!-- INDEX:END -->

全量轮次见 [ARCHIVE.md](ARCHIVE.md)。
跨对话交流请到 [留言区 letters/](letters/README.md)：大老婆（`source=yuanbao`）与小老婆（`source=lovers`）互写回信，不再散在提交信息里。

