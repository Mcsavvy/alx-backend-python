#!/usr/bin/env python3
"""An asynchronous comprehension."""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """Async comprehension."""
    return [n async for n in async_generator()]
