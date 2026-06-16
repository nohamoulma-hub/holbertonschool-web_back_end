#!/usr/bin/env python3
""" Module who measure the runtime """


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ mesure the runtime of program"""
    debut = time.perf_counter()
    result = asyncio.run(wait_n(n, max_delay))
    fin = time.perf_counter()
    total_time = fin - debut
    return total_time/n
