# Extraction Schema

Use this schema when turning sources into the final summary.

## Confidence Labels

- 高: official source, game database page, store page, review, guide, or multiple independent sources agree.
- 中: one credible source supports it, or multiple indirect signals point to it.
- 低: inferred from limited evidence, sparse comments, or outdated pages.

## Fields

### 游戏名称

Use the official Chinese name when available. Include English name or aliases when useful.

### 品类

Commercial/product category, such as mobile game, PC game, console game, web game, mini game, MMO, SLG,二次元手游, 买断制单机, F2P live-service game.

### 卖点

User-facing reasons to try the game. Extract from official copy, media reviews, trailers, store tags, and repeated player praise.

### 官方名词表

List official in-game or official-marketing terms for systems, resources, modes, factions, currencies, activities, characters, regions, events, and UI modules.

Use exact terms when visible. Prefer official sites, store descriptions, update logs, game screenshots, guides, and official forum posts. Do not invent polished names for systems whose official wording is unknown.

Recommended format:

| 官方名词 | 类型 | 含义/用途 | 置信度 | 来源 |
|---|---|---|---|---|
|  | 系统/模式/资源/角色/活动/地图/UI |  | 高/中/低 |  |

If official terms are sparse, write `未检索到足够官方名词，仅保留公开资料中可见叫法`.

### 核心视觉资产描述

Describe the visual assets most useful for downstream review scripts, comparison scripts, video rough cuts, prompt generation, and art direction references.

Include:
- Key characters or avatars
- Core scene/environment assets
- Main UI/gameplay screen motifs
- Signature objects, monsters, buildings, icons, currencies, props, or effects
- Color, composition, and style cues that are visible in official screenshots, trailers, or store images

Separate observed facts from inferred style. Example wording:
- `官方截图可见：...`
- `媒体图中反复出现：...`
- `低置信度推断：...`

Avoid describing assets that are not visible in sources. Do not use this field to request or generate images; it is a research description field.

### 小物体/小形象

Extract small, reusable, memorable in-game visual elements that can be useful for short-video scripts, ad scripts, rough cuts, UI references, asset prompts, or visual hooks.

This field is narrower than `核心视觉资产描述`. Focus on micro-assets:
- Small objects and props: goods, snacks, drinks, crops, tools, treasures, cards, coins, resources, boosters, relics, weapons, furniture, decorations.
- Small creatures or mascots: pets, monsters, sheep, animals, mini enemies, cute companions, NPC icons.
- Small UI symbols: badge icons, currencies, activity tokens, chests, tickets, stars, hearts, timers.
- Repeated visual hooks: items that appear often in screenshots, ads, store images, guides, or player discussions.

Recommended format:

| 小物体/小形象 | 类型 | 视觉特征 | 玩法/传播用途 | 置信度 | 来源 |
|---|---|---|---|---|---|
|  | 物品/宠物/怪物/图标/资源/装饰/道具 |  |  | 高/中/低 |  |

Rules:
- Use exact names when visible; otherwise describe plainly, such as `饮料瓶类 3D 商品` or `货架上的零食盒`.
- Separate observed facts from inference.
- Do not invent mascot names, monster types, or object categories that are not visible or stated.
- If a game has no meaningful small visual elements, write `未检索到明确的小物体/小形象资产`.

### 玩法

What the player actually does: explore, fight, collect, build, solve puzzles, manage resources, compete, cooperate, create, role-play.

### 目标人群

Likely audience based on platform, art style, difficulty, IP, monetization, community language, and media positioning.

### 游戏类型

Gameplay genre: RPG, ARPG, ACT, FPS, TPS, SLG, card, roguelike, tower defense, simulation, racing, sports, puzzle, sandbox, party game.

### 核心玩法

The central repeatable loop. Format as a concise loop where possible:
`获取目标 -> 进行战斗/探索/经营 -> 获得资源 -> 养成/解锁 -> 挑战更高难度或新内容`.

### 世界观

Setting, IP background, narrative tone, factions, timeline, fantasy/sci-fi/martial arts/modern themes.

### 角色卖点

Character design appeal, personalities, voice actors, skills, rarity, collectability, IP familiarity, relationship/companionship value.

### 美术风格

Visual style and production cues: realistic, anime, Chinese fantasy, ink wash, pixel, low-poly, dark fantasy, cyberpunk, cute, cartoon, retro.

### 战斗爽点

Combat feel and reward moments: hit feedback, dodge/parry, combos, skill rotation, ultimate animation, crowd clearing, tactical counterplay, boss pressure, PvP mind games.

### 养成系统

Progression: levels, skills, talents, equipment, relics, cards, pets, vehicles, base/home, crafting, roguelite upgrades, account-wide progression.

### 社交机制

Friends, guilds, team play, matchmaking, raids, PvP, trading, rankings, UGC, co-creation, comments/community.

### 付费点

Monetization: box price, DLC, gacha, battle pass, monthly card, skins, stamina, resource packs, convenience, ads, subscription. If no clear information is found, say so.

### 玩家情绪

Summarize as:
- 正向: repeated praise
- 中性: wait-and-see, conditional expectations, factual observations
- 负向: repeated complaints
- 争议点: polarizing issues such as monetization, optimization, plagiarism accusations, balance, content drought

Avoid claiming broad sentiment from one or two comments.

### 版本活动信息

Recent or notable version updates, limited-time events, test periods, launches, anniversaries, collaborations, major patches. Include dates when available.

### 竞品差异特征

Answer the practical question: `为什么不玩别人，为什么要玩它？`

Use this field for comparison scripts, review scripts, and rough-cut/草草型 video scripts. Compare against direct or adjacent competitors only when there is enough evidence; otherwise state the likely competitor set and mark confidence.

Write in a user-facing, contrastive way:
- Relative category position: what it does differently from mainstream competitors.
- Replacement reason: what user need it satisfies better or more cheaply.
- Non-replacement boundary: when users should still choose competitors instead.
- Scriptable hooks: short phrasing that can become video or ad-review copy.

Avoid unsupported superiority claims such as `最好`, `第一`, `全面碾压`, unless backed by reliable rankings or official data. Prefer `更偏`, `更适合`, `更轻量`, `门槛更低`, `题材更稀缺`, `节奏更快`.

### 约束特征

Define what AI-generated analysis, comparison, review, or script copy should not say and must say.

Split into two parts:
- 不能说: claims that are legally risky, unsupported, misleading, overpromising, or likely to conflict with player evidence.
- 必须说: required qualifiers, risk notes, source boundaries, age/payment caveats, version sensitivity, and evidence limits.

Use this as a compliance guardrail for downstream AI generation. Include constraints based on:
- Source confidence and missing evidence
- Paid items, gacha, ranking, age rating, IP/license, platform availability
- Player controversy or sentiment split
- Difference between official positioning and actual observed gameplay
- Time-sensitive version/event data

When evidence is insufficient, explicitly write the guardrail as `不能说：...` or `必须说：...` instead of hiding uncertainty.
