#!/usr/bin/env python3
"""
Generate search-query candidates for game industry research.

This helper intentionally does not scrape websites directly. It prints stable,
domain-limited queries that an agent can run through web search or a browser.
"""

from __future__ import annotations

import argparse
from urllib.parse import quote_plus


DOMAINS = [
    "17173.com",
    "3dmgame.com",
    "7k7k.com",
    "4399.cn",
    "ali213.net",
    "gamersky.com",
    "taptap.cn",
]

INTENTS = [
    ("basic", "{game} 游戏库 OR 专区 OR 资料"),
    ("official_terms", "{game} 系统 OR 模式 OR 资源 OR 活动 OR 官方 名词"),
    ("visual_assets", "{game} 截图 OR 美术 OR 角色 OR UI OR 场景"),
    ("small_assets", "{game} 小物件 OR 道具 OR 宠物 OR 怪物 OR 图标 OR 资源 OR 装饰"),
    ("review", "{game} 评测 OR 试玩 OR 测评"),
    ("gameplay", "{game} 玩法 OR 攻略 OR 养成 OR 战斗"),
    ("operation", "{game} 版本 OR 活动 OR 更新 OR 公告"),
    ("sentiment", "{game} 评论 OR 评价 OR 评分 OR 玩家"),
]

OVERSEAS_INTENTS = [
    ("official", "{game} official site"),
    ("steam", "site:store.steampowered.com {game}"),
    ("metacritic", "site:metacritic.com {game}"),
    ("reddit", "site:reddit.com {game} review OR impressions"),
]


def build_queries(game: str, include_overseas: bool) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for domain in DOMAINS:
        for intent, pattern in INTENTS:
            query = f"site:{domain} {pattern.format(game=game)}"
            rows.append((domain, intent, query))
    if include_overseas:
        for intent, pattern in OVERSEAS_INTENTS:
            rows.append(("overseas", intent, pattern.format(game=game)))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("game", help="Game name to research")
    parser.add_argument("--overseas", action="store_true", help="Include overseas supplemental queries")
    parser.add_argument("--urls", action="store_true", help="Print search URLs instead of raw queries")
    args = parser.parse_args()

    for domain, intent, query in build_queries(args.game, args.overseas):
        if args.urls:
            value = f"https://www.google.com/search?q={quote_plus(query)}"
        else:
            value = query
        print(f"{domain}\t{intent}\t{value}")


if __name__ == "__main__":
    main()
