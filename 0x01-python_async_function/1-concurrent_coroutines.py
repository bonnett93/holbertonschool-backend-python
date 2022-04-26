#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """
    wait_list = []
    courutines = []

    for i in range(n):
        courutines.append(wait_random(max_delay))

    for task in asyncio.as_completed(courutines):
        earliest_result = await task
        wait_list.append(earliest_result)

    return wait_list
