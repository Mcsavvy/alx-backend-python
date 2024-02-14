#!/usr/bin/env python3
"""Running concurrent coroutines."""
import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


def task_wait_n(n: int, max_delay: int):
    """Wait for `task_wait_random(max_delay)` n times."""

    async def sub_coro():
        return await task_wait_random(max_delay)

    async def main_coro():
        results = list(await asyncio.gather(*[sub_coro() for _ in range(n)]))
        results.sort()
        return results

    return main_coro()
