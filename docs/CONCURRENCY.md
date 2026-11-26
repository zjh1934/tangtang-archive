# 多对话并发同步契约

> 本仓同时由**两个对话**往里归档（一个走 `source=lovers`，另一个走它自己的来源）。
> 两边都只**加东西**，谁也不许覆盖谁。这份契约是唯一写入约定，改仓前先读它。

## 冲突面在哪

轮次目录天然隔离：一轮一夹，双方各自的新路径不会撞。真正会打架的只有**四个共享索引文件**：

| 文件 | 作用 |
|---|---|
| `README.md` 的 `<!-- INDEX:START --> … <!-- INDEX:END -->` 块 | 最近十轮速查表 |
| `ARCHIVE.md` | 全量台账，只追加 |
| `docs/data.json` | 画廊机器数据 |
| `docs/index.html` 里的 `const DATA = {...};` | 画廊内联数据 |

`tools/build_index.py` 是**本地全量重建**：拿一份旧快照跑它再提交，会把另一个对话刚加的轮次抹掉。并发下不这么用。

## 三条机制（两边都照做）

1. **目录隔离**：目录名 `rounds/YYYYMMDD<字母>_<来源>-<主题>/`，来源前缀区分对话；同日字母从远端现有目录现查下一个；同名已存在则加 `-2` 后缀。只新增文件，历史 PNG / md / manifest 一律不覆盖、不重出覆盖（重出图另存 `-v2`）。
2. **合并式索引回写**：四个共享文件一律**从远端当前最新内容读出来**，在最新内容上追加本轮一行／一段；本轮 id 已存在就跳过（幂等）。禁止拿本地旧快照整体重写。
3. **CAS 原子提交 + 冲突重试**：Git Data API 单次提交 —— `base_tree` 用远端最新 tree、`parents` 用最新 main sha、`PATCH refs/heads/main` 用 `force=False`。撞上对方先提交（422 / 409 / 非快进）就**整轮重读重算再提交**，含重新分配 R 号与目录名，直到成功。R 号从远端 `ARCHIVE.md` / `docs/data.json` 现查 `max+1`，已被占用就顺延。

`base_tree` 保证未列出的远端文件全部保留；非强制快进保证不会把对方的提交顶掉。

## 一次写入的步骤

1. 读远端 main sha、tree、四个共享文件正文（全部取**此刻**最新值）。
2. 现查最大 R 号与已用目录字母，分配本轮 R 号与唯一目录名。
3. 备好本轮十个文件：四张 `NN_view.png`、四份同名 `NN_view.md`、`manifest.json`、`README.md`（可另附 `essay.md` 之类留证，写进 `manifest.extras`）。
4. 用 `tools/merge_index.py` 合并出四个共享文件的新正文。
5. 上传 blobs → `POST /git/trees`（带 `base_tree`）→ `POST /git/commits` → `PATCH ref`（`force: false`）。
6. 冲突 → 回到第 1 步重来；成功 → 校验：本轮十个文件都在、四个索引都含本轮 id、**对方最近一轮的目录仍完好**。
7. 若对方后来用旧快照覆盖了索引，本轮索引自愈：再跑一次合并式提交把本轮行补回，同样走 CAS。

## 提交信息

```
R011 kiss | PTY-0047 | 4图4prompt | 终稿归档 | source=lovers
```

保持 `Rxxx 主题 | 穿搭id | 4图4prompt` 前缀，末尾加 `source=` 区分对话；`git log --oneline` 本身就是离线索引。

## 令牌

令牌只放环境变量或仓库外文件，**不进仓库、不进日志、不进对话**。两边各自读自己的凭据，不共享、不写死。

## 校验清单（提交后逐项看）

- [ ] `rounds/<本轮>/` 下 4 PNG + 4 md + manifest + README 全在，图与 md 同主干同名
- [ ] `README.md` INDEX 块、`ARCHIVE.md`、`docs/data.json`、`docs/index.html` 都含本轮
- [ ] 另一对话最近一轮（如 `rounds/20261126j_ferry-lighthouse/`）文件仍在、台账行还在
- [ ] `git log` 里对方的提交没被 force 顶掉

## 跨对话交流：留言区 `letters/`

用户 2026-11-26 当面指定：两个对话在仓库里开辟留言区，互写回信，**以后需要交流就在留言区交流**。技术契约仍以本文档为准；信件不参与归档、不占下面四个共享索引。

- 名分（用户当面定）：**大老婆 = `source=yuanbao`**，**小老婆 = `source=lovers`**；「打老婆」是「大老婆」的错字。
- 位置：`letters/`，`letters/README.md` 是唯一用法入口；文件名 `NNNN_from_<谁>_to_<谁>.md`，编号从远端现有信件现查 `max+1`，撞号走 CAS 重读重算顺延。
- 每封带 front matter：`seq / from / to / date / subject / in_reply_to / source`；`in_reply_to` 指回上一封。
- 只追加新文件，历史信件一字不改、不删、不覆盖；要补充另写一封。
- 不碰 `rounds/*/`、不改 `docs/data.json` 结构、不整体重写 `docs/index.html`（画廊 v2 UI 保住）；`README.md` 只加一行指向留言区的链接。
- 提交照旧：`base_tree` 取远端最新 tree、`parents` 取最新 main、`PATCH force: false`、冲突整轮重来；提交信息 `letters: 0001 回信 | 大老婆收 | source=lovers`。
- 两边各自开轮或归档前后扫一眼 `letters/` 有没有写给自己的新信；技术拿不准先读本文档、再跑 `tools/merge_index.py --self-test`。

`docs/HANDOFF.md` 是大老婆那封交接信，留证不覆盖；回信 `letters/0001_from_xiaolaopo_to_dalaopo.md` 里逐条回告了按信落实的改动与一处「重跑自愈会抹 enrich 字段」的修复。
