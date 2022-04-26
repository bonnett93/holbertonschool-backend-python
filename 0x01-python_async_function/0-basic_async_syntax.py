#!/usr/bin/env python3
"""
Module: 0-basic_async_syntax asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes in an integer argument (max_delay, with a default value of 10),
    waits for a random float delay between [0 and max_delay]
    seconds and eventually returns it.
    """
    wait_random = random.uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return wait_random
