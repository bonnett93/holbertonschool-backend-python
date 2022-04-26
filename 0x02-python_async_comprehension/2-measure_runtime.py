#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    t will execute async_comprehension four times in parallel
    using asyncio.gather. measure the total runtime and return it.
    """
    s = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    total_time = time.time() - s
    return total_time
