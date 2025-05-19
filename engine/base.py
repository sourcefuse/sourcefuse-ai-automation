# framework/base.py
import asyncio
import importlib
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use.agent.service import Agent
from config import settings
from engine.reporter import Reporter

class BaseEngine:
    def __init__(self, tasks=None, use_vision=True):
        self.tasks = tasks if tasks else []
        self.use_vision = use_vision
        self.llm = self._initialize_llm()
        self.reporter = Reporter()  # Initialize the Reporter

    def _initialize_llm(self):
        api_key = settings.gemini_api_key
        return ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

    async def run_single_task(self, task):
        agent = Agent(task, self.llm, use_vision=self.use_vision)
        history = await agent.run()
        # return history.final_result()
        final_result = history.final_result()

        # Ensure the result is a dictionary with "status" and "details" keys
        if isinstance(final_result, str):
            return {"status": "success", "details": final_result}
        elif isinstance(final_result, dict):
            return final_result
        else:
            return {"status": "unknown", "details": str(final_result)}

    async def run_all_tasks(self):
        results = []
        for task in self.tasks:
            result = await self.run_single_task(task)
            results.append((task, result))

        # Generate reports
        self.reporter.save_json_report(results)
        self.reporter.save_csv_report(results)
        self.reporter.save_html_report(results)  # Generate HTML report
        return results

    @staticmethod
    def load_tasks_from_module(module_name):
        module = importlib.import_module(module_name)
        tasks = []
        for attr in dir(module):
            if attr.startswith("TASK_") or attr.endswith("_TASK"):
                tasks.append(getattr(module, attr))
        return tasks