#!/isr/bin/env python3
""" Module who write an asynchronous
coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """creation of asynchronous coroutine who
    takes a delay random between 0 to 10s """

    delay = random.uniform(0, max_delay)
    return delay
