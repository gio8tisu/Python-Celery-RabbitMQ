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
        # sleep 10 seconds to ensure the task has been finished
        res = result.get(timeout=10)
        # now the task should be finished and ready method will return True
        print("Task finished?", result.ready())
        print("Task result:", res)
