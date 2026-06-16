#!/usr/bin/env python3
""" Module  execute multiple
coroutines at the same time with async """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    # Liste qui va stocker les délais, dans l'ordre où ils se terminent
    delays = []
    # On crée n coroutines wait_random(max_delay) d'un coup
    tasks = [wait_random(max_delay) for _ in range(n)]

# asyncio.as_completed planifie toutes les tasks pour qu'elles
# s'exécutent en concurrence, puis elle les redonne une par une,
# dans l'ordre où elles FINISSENT (pas dans l'ordre de création).
# C'est ce qui permet d'avoir une liste triée sans appeler sort().
    for task in asyncio.as_completed(tasks):
        # await récupère la valeur de retour de la task une fois
        # qu'elle est terminée (ici : le délai généré aléatoirement)
        result = await task
        delays.append(result)
    return delays
