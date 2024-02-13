#!/usr/bin/env python3
"""Measure Runtime."""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """Measure the runtime of async function called 4 times."""
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start
