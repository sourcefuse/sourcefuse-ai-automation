# run.py
import asyncio
import os
import importlib
from engine.base import BaseEngine

def discover_tests(test_dir="tests"):
    test_files = []
    for file in os.listdir(test_dir):
        if file.endswith(".py") and not file.startswith("__"):
            test_files.append(f"{test_dir}.{file[:-3]}")
    return test_files

async def main():
    test_files = discover_tests()
    all_tasks = []
    for test_file in test_files:
        tasks = BaseEngine.load_tasks_from_module(test_file)
        all_tasks.extend(tasks)

    if not all_tasks:
        print("No tasks found in test files.")
        return

    framework = BaseEngine(all_tasks)
    test_results = await framework.run_all_tasks()

    for task, result in test_results:
        print(f"Task: {task}")
        print(f"Result: {result}")
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())