# run_single_test.py
import asyncio
import importlib
from engine.base import BaseEngine


async def main(test_module, test_name):
    try:
        # Dynamically import the test module
        module = importlib.import_module(test_module)

        # Get the task from the module
        task = getattr(module, test_name, None)
        if not task:
            print(f"Error: Task '{test_name}' not found in module '{test_module}'.")
            return

        # Run the single task
        framework = BaseEngine([task])
        test_results = await framework.run_all_tasks()

        for task, result in test_results:
            print(f"Task: {task}")
            print(f"Result: {result}")
            print("-" * 40)

    except ImportError:
        print(f"Error: Module '{test_module}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 run_single_test.py <test_module> <test_name>")
        print("Example: python3 run_single_test.py tests.test_login LOGIN_TASK")
        sys.exit(1)

    test_module = sys.argv[1]  # e.g., "tests.test_login"
    test_name = sys.argv[2]  # e.g., "LOGIN_TASK"

    asyncio.run(main(test_module, test_name))