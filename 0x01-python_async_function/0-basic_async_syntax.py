"""A simple asynchronous coroutine."""
import asyncio
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and
    max_delay seconds and returns it."""
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay