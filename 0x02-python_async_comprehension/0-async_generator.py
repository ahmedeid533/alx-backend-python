#!/usr/bin/env python3
""" Defines an async generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loops 10 times, yielding a random number 
    between 0 and 10 
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)