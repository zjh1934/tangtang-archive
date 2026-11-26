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
