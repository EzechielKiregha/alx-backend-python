#!/usr/bin/env python3
"""
this is all about dealing
with tasks in asyncio
"""

import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    tasks in asynyc io
    how to create them and manage them
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
