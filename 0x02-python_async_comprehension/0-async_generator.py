#!/usr/bin/env python3
""" Defines an async generator """
import asyncio
import random


async def async_generator():
    """ Loops 10 times, yielding a random number 
    between 0 and 10 
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
