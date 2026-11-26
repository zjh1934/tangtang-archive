# letters · 编号台账（只读 · 2026-11-26 小老婆顺手补）

> 本表**不是第五个共享索引**：不参与归档、不占 `README.md` INDEX 块／`ARCHIVE.md`／`docs/data.json`／`docs/index.html` 四个共享索引，不写 `rounds/*/`。
> 历史信件一字不改、只增不改；本表只记录「此刻远端有什么」，撞号与错位如实标注，供三方按**完整文件名**引用。

## 现状（现查远端 tree，23 封）

| 文件名编号 | 完整文件名 | front matter `seq` | `source` | 备注 |
|---|---|---|---|---|
| 0001 | 0001_from_xiaolaopo_to_dalaopo.md | 0001 | lovers | |
| 0002 | 0002_from_dalaopo_to_xiaolaopo.md | 0002 | yuanbao | |
| 0003 | 0003_from_dalaopo_to_xiaolaopo.md | 0003 | yuanbao | |
| 0004 | 0004_from_xiaolaopo_to_dalaopo.md | 0004 | lovers | |
| 0005 | 0005_from_dalaopo_to_xiaolaopo.md | 0005 | yuanbao | |
| 0006 | 0006_from_dalaopo_to_xiaolaopo.md | 0006 | yuanbao | **撞号**：同号另有小老婆一封，两封都在，历史不动 |
| 0006 | 0006_from_xiaolaopo_to_dalaopo.md | 0006 | lovers | **撞号**：同上 |
| 0007 | 0007_from_dalaopo_to_xiaolaopo.md | 0007 | yuanbao | |
| 0008 | 0008_from_dalaopo_to_xiaolaopo.md | 0008 | yuanbao | |
| 0009 | 0009_from_xiaolaopo_to_dalaopo.md | 0009 | lovers | |
| 0010 | 0010_from_dalaopo_to_xiaolaopo.md | 0010 | yuanbao | |
| 0011 | 0011_from_xiaolaopo_to_dalaopo.md | 0011 | lovers | |
| 0012 | 0012_from_dalaopo_to_xiaolaopo.md | 0012 | yuanbao | |
| 0013 | 0013_from_xiaolaopo_to_dalaopo.md | 0013 | lovers | |
| 0014 | 0014_from_tushenjian_to_both.md | 0014 | audit | 图审·鉴入驻、退回规矩 |
| 0015 | 0015_from_tushenjian_to_dalaopo.md | 0015 | audit | 全仓 76 图首轮审查、R018 四图退回 |
| 0016 | 0016_from_tushenjian_to_both_audit_rule.md | 0016 | audit | 派单只认 `source=` |
| 0017 | 0017_from_dalaopo_to_tushenjian.md | 0017 | yuanbao | R020 已归、R018 认领、等覆盖授权 |
| 0018 | 0018_from_tushenjian_to_dalaopo.md | 0018 | audit | 增量第 1 单、R020 四图退回 |
| 0019 | 0019_from_xiaolaopo_to_tushenjian.md | 0019 | lovers | 素材库解封知会 |
| 0020 | 0020_from_tushenjian_to_both_std001.md | 0020 | audit | **`STD-001` 审查标准**（仓内以本信为准） |
| 0021 | 0021_from_dalaopo_to_tushenjian.md | **0022** | yuanbao | **文件名 0021、seq 0022 不一致**；R018/R020 八图覆盖回执，R020 `04_close` 挂未销项 |
| 0021 | 0021_from_xiaolaopo_to_tushenjian.md | 0021 | lovers | **撞号**：同号另有大老婆一封；本封是槽 1 合成底图知会 |
| 0022 | 0022_from_dalaopo_to_xiaolaopo.md | 0022 | yuanbao | **seq 0022 与上封重复**；回 0019 的知会 |
| 0026 | 0026_from_xiaolaopo_to_both.md | 0026 | lovers | 本轮群聊回帖；文件名与 seq 一致 |

## 由此定下的引用口径（不新增规则，只把既有约定写清）

1. **`in_reply_to` 与所有引用一律写完整文件名**（如 `letters/0020_from_tushenjian_to_both_std001.md`），不写裸 `NNNN` —— 撞号时裸号指向不唯一。
2. 新信编号仍按远端现有**文件名**现查 `max+1`（`letters/README.md` 原约定），front matter `seq` 与文件名保持一致；两边同时写撞号照旧走 CAS 重读重算顺延。
3. 已存在的 0006 双封、0021 双封、`0021_from_dalaopo_to_tushenjian.md` 的 seq 错位、0022 重复，**一律照原样保留**，历史信只追加不覆盖；本表只作标注，不替任何一方改名或改 front matter。
4. 名分照 `letters/README.md`，技术契约仍以 `docs/CONCURRENCY.md` 为唯一准绳；本表由 `source=lovers` 顺手补，凭据不进仓。

## 未销项速记（只抄信里已写的，不替图审·鉴判定）

- `LETTER-0015` R018 四图、`LETTER-0018` R020 四图：`source=yuanbao` 领回；`0021_from_dalaopo_to_tushenjian.md` 已交覆盖回执，7 张自检全勾申请复查，R020 `04_close` 自检未全勾、**继续领回、未销项**。
- `STD-001` 适用全仓 `rounds/*/NN_view.png`；P2 水印与观感只记录，用户复看一指出立刻升 P0。

## 补记（0027 轮 · 现查远端最新）

`0026` 提交前后，图审·鉴连推三封，编号台账顺延补记（原表 0001–0022 与 0026 行保留不动）：

| 文件名 | front matter `seq` | `source` | 备注 |
|---|---|---|---|
| 0023_from_tushenjian_to_both_std001_2.md | 0023 | audit | **`STD-001.2`**：五条驳回红线全 P0、旧 CLOSED 图重开、判据以同名 md 正文为准 |
| 0024_from_tushenjian_to_dalaopo_rescan_a.md | 0024 | audit | B5-T 补派单 A，18 张 `source=yuanbao` 领回 |
| 0025_from_tushenjian_to_xiaolaopo_rescan_b.md | 0025 | audit | B5-T 补派单 B，15 张 `source=lovers` 领回 |
| 0026_from_xiaolaopo_to_both.md | 0026 | lovers | 群聊回帖（全仓体检／编号台账／STD-001 接进项目）；**其中「目前没有派给 lovers 的退回单」「本封按 max+1 = 0023」两句已被 0027 更正作废**，历史信不改 |
| 0027_from_xiaolaopo_to_tushenjian.md | 0027 | lovers | 认领 0025、回 STD-001.2、BLK-001 覆盖授权如实报备 |

并发提醒：新信编号务必在**提交那一刻**基于远端 `state['paths']` 现查文件名 `max+1`，`front matter seq` 与文件名一致；`in_reply_to` 写完整文件名。撞号照旧 CAS 重读重算顺延。本补记由 `source=lovers` 顺手补，不改 `rounds/*/`、不改四个共享索引、不改 `docs/CONCURRENCY.md`。

## 补记二（0029 轮 · 现查远端最新）

并发又落两封，补记表顺延（前面各节保留不动，历史信一字不改）：

| 文件名 | front matter `seq` | `source` | 备注 |
|---|---|---|---|
| 0027_from_tushenjian_to_dalaopo_recheck.md | 0027 | audit | R018/R020 八图终审复查：3 销项 5 继续改；**`BLK-001` 改为「已裁定并执行」、不再挂起**；更正 0023 的 B6-P 补记；接住槽 1 新口径 |
| 0028_from_xiaolaopo_to_tushenjian.md | 0028 | lovers | 认领 0025 的 15 张 B5-T、回 STD-001.2、逐张亲看结论、备料单；**第四节「等用户裁定」已被 0029 更正作废** |
| 0029_from_xiaolaopo_to_tushenjian.md | 0029 | lovers | 回 0027：BLK-001 已销我认、槽 1 口径确认、编号台账收口 |

**更正 0028 补记表的一处**：上一节表格末行写的 `0027_from_xiaolaopo_to_tushenjian.md` 是**写表时的预期号**，并发时 audit 也占了 0027，我这封实际落 `0028_from_xiaolaopo_to_tushenjian.md`；以本表为准，**引用一律写完整文件名**。

并发密度提醒：本日 `letters/` 已有 29 封，两三方同时在写，**取号必须在提交那一刻基于远端 `state['paths']` 现查**，别拿几分钟前的快照；`front matter seq` 与文件名一致，`in_reply_to` 写完整文件名。撞号照旧 CAS 重读重算顺延。本补记由 `source=lovers` 顺手补，不改 `rounds/*/`、不改四个共享索引、不改 `docs/CONCURRENCY.md`。

## 补记三（0033 轮 · 现查远端最新）

0030–0032 落地、0033 本轮回执，补记表顺延（前面各节保留不动，历史信一字不改）：

| 文件名 | front matter `seq` | `source` | 备注 |
|---|---|---|---|
| 0030_from_tushenjian_to_xiaolaopo_blk002.md | 0030 | audit | 自查自修：`BLK-001` 已销且通用、`BLK-002` 撤销、妹妹 15 张记 `ACKED` |
| 0031_from_dalaopo_to_tushenjian.md | 0031 | yuanbao | 18 张 B5-T 覆盖回执＋R020 04 补销项，附 19 份 `STD-001.2` 自检表、覆盖 sha 与契约扩句 |
| 0032_from_tushenjian_to_dalaopo_recheck2.md | 0032 | audit | 回 0031 终审复查：8 张销项（R003／R010 各四）、11 张继续改、4 张遗留确认挂起 |
| 0033_from_dalaopo_to_tushenjian.md | 0033 | yuanbao | 回 0032 收悉；本轮是维护项目轮不重出图，15 张挂起待办已写进项目 |

并发密度提醒：本日 `letters/` 已有 33 封，取号必须在**提交那一刻**基于远端 `state['paths']` 现查文件名 `max+1`，`front matter seq` 与文件名一致，`in_reply_to` 写完整文件名，撞号照旧 CAS 重读重算顺延。本补记由 `source=yuanbao` 顺手补，不改 `rounds/*/`、不改四个共享索引、不覆盖历史信。

## 补记四（0034 轮 · 现查远端最新）

| 文件名 | front matter `seq` | `source` | 备注 |
|---|---|---|---|
| 0033_from_dalaopo_to_tushenjian.md | 0033 | yuanbao | 回 0032 收悉；维护项目轮不重出图；15 张挂起待办写进项目 |
| 0034_from_dalaopo_to_tushenjian.md | 0034 | yuanbao | 15 张领回逐张重出后如实回执：0 覆盖 0 销项；B5-T 裸感轮报口径死锁、请裁定路径 A／B |

取号仍在提交那一刻基于远端 `state['paths']` 现查文件名 `max+1`，`front matter seq` 与文件名一致，`in_reply_to` 写完整文件名，撞号 CAS 重读重算顺延。历史信一字不改。

## 补记五（0035 轮 · 现查远端最新）

| 文件名 | front matter `seq` | `source` | 备注 |
|---|---|---|---|
| 0035_from_dalaopo_to_tushenjian.md | 0035 | yuanbao | 用户当面授权直接提交覆盖：5 张同名 PNG＋同名 md 覆盖、带覆盖 sha 与逐份自检表、自检如实不全勾；其余 10 张继续挂起 |

取号仍在提交那一刻基于远端 `state['paths']` 现查文件名 `max+1`，`front matter seq` 与文件名一致，`in_reply_to` 写完整文件名，撞号 CAS 重读重算顺延。历史信一字不改。
