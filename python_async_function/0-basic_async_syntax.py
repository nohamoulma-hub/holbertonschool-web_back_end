#!/isr/bin/env python3
""" Module who write an asynchronous
coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    return delay
