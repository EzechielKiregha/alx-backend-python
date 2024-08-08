#!/usr/bin/env python3
"""
The AsyncIO
"""

import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """tasks in asynyc io
    how to create them and manage them

    Args:
        max_delay (int): specific delay time

    Returns:
        asyncio.Task: Async Task is returned
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
