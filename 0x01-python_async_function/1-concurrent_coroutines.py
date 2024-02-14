#!/usr/bin/env python3
"""Running concurrent coroutines."""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for `wait_random(max_delay)` n times."""

    async def coro():
        return await wait_random(max_delay)

    results = list(await asyncio.gather(*[coro() for _ in range(n)]))
    results.sort()
    return results
