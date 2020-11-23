#!/usr/bin/env python

import time
import argparse

from test_celery import tasks


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--times", type=int, default=1)

    args = parser.parse_args()

    for _ in range(args.times):
        result = tasks.longtime_add.delay(1, 2)
        # at this time, our task is not finished, so it will return False
        print("Task finished?", result.ready())
        print("Task result:", result.result)
        res = result.get(timeout=10)
        print("Task finished?", result.ready())
        print("Task result:", res)
