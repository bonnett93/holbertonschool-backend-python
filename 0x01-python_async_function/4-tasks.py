#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """
    wait_list = []
    courutines = [task_wait_random(max_delay) for i in range(n)]

    for task in asyncio.as_completed(courutines):
        earliest_result = await task
        wait_list.append(earliest_result)

    return wait_list
