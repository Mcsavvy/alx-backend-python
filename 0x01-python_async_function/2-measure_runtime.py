#!/usr/bin/env python3
"""Measure runtime of async coroutines."""

import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure runtime of async coroutines."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    if n <= 0:
        return 0.0
    return (time.perf_counter() - start) / n
