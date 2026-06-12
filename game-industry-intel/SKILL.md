---
name: game-industry-intel
description: Use when a user wants to research a game by name and produce a Markdown game intelligence summary from Chinese game media and community sources, with optional overseas sources. Covers game category, selling points, official in-game terminology, core visual assets, small in-game objects/mascots, gameplay, target audience, core loop, worldbuilding, character appeal, art style, combat appeal, progression, social systems, monetization, player sentiment, version events, competitive differentiation, and AI-script compliance constraints.
---

# Game Industry Intel

Use this skill to research a game by name and create a local Markdown summary document.

## Inputs

Ask for missing details only when ambiguity would materially change the result. Otherwise proceed with reasonable assumptions.

Useful user inputs:
- Game name
- Optional platform: mobile, PC, console, web, mini game
- Optional market scope: China first, overseas supplement, global
- Optional time range
- Optional focus: monetization, player sentiment, gameplay, competitors, version operation, review script, comparison script, rough-cut script

## Source Priority

Prioritize Chinese game industry and player-facing sources:
- 17173: online games, mobile games, new games, rankings, tests, version news
- 3DM: PC, console, single-player games, reviews, guides, news
- 7k7k: mini games, web games, younger/lightweight audience signals
- 4399: mobile games, mini games, web games, youth-oriented game signals
- Ali213: PC, console, mobile, guides, topics, game database
- Gamersky: PC, console, single-player games, reviews, guides, topics
- TapTap: mobile games, ratings, community reviews, updates, player sentiment

Use overseas or general sources as supplements when domestic sources are thin or the game is overseas-first:
- Official game website
- Steam store/community/news
- PlayStation, Xbox, Nintendo store pages
- Metacritic/OpenCritic
- Wikipedia or Fandom only for basic world/IP context
- Reddit, Discord excerpts, YouTube descriptions, or overseas media only when clearly useful

See `references/source_strategy.md` for source-specific tactics.

## Research Workflow

1. Normalize the game entity.
   - Identify standard Chinese name, English name, aliases, abbreviations, and franchise ambiguity.
   - If multiple games share the name, choose the most likely match from the user's context or ask one concise clarification.

2. Search broadly, then narrow.
   - Start with domain-limited queries such as `site:taptap.cn 游戏名`, `site:gamersky.com 游戏名 评测`, `site:17173.com 游戏名 版本 活动`.
   - Prefer game database, official, topic, review, update, guide, and community pages over low-signal reposts.
   - Use browser access for dynamic pages, especially TapTap and modern app-like pages.

3. Select evidence.
   - Keep 5-12 high-signal sources when possible.
   - Include at least one source for basic info, one for gameplay/system information, one for version/operations if available, and one for player sentiment if available.
   - Deduplicate syndicated or copied articles.

4. Extract into the schema.
   - Follow `references/extraction_schema.md`.
   - Distinguish direct facts from synthesized conclusions and inferred judgments.
   - Mark uncertain fields as `未检索到明确资料` or `低置信度推断`.
   - In product positioning, always include official terminology, core visual assets, and small in-game objects/mascots when source material supports them.
   - Always include competitive differentiation and constraint features for downstream comparison, review, and AI-generated script usage.

5. Generate the Markdown document.
   - Use `references/markdown_template.md`.
   - Save the final file as `<游戏名>-游戏信息总结.md` unless the user specifies another path.
   - Put the document in the current workspace or the user-requested directory.

## Evidence Rules

- Do not invent details for fields that are not supported by sources.
- Cite source links in the source list and, where useful, next to important claims.
- Use confidence labels: `高`, `中`, `低`.
- For player sentiment, use `正向 / 中性 / 负向 / 争议点`. Do not force numeric ratios unless there is enough visible comment volume and the user asks for quantification.
- If a conclusion is synthesized from multiple pages, say so plainly.
- If information is likely stale or version-sensitive, include retrieval date or page publish/update date when available.
- For constraint features, separate factual compliance limits from recommended wording guardrails. Do not create legal claims unless the source supports them.
- For official terminology, preserve the exact Chinese/English term when visible in official pages, update notes, screenshots, or guides. Do not rename systems casually.
- For visual assets, describe what can be seen or reliably inferred from official images, store screenshots, videos, or media screenshots. Do not fabricate unobserved UI or character details.
- For small in-game objects/mascots, focus on recognizable small items, props, tokens, cute creatures, mini characters, icons, goods, collectibles, crops, pets, monsters, decorations, and other reusable micro-assets. Mark whether each item is directly observed or inferred.

## Optional Script

If many searches are needed, use or adapt `scripts/collect_game_pages.py` to generate search-query candidates and save a lightweight source table. The script is a helper, not a required crawler; browser and web search may still be more reliable for dynamic pages.
