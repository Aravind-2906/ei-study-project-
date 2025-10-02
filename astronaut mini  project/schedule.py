from typing import List
import threading
from task import Task
import logging

logger = logging.getLogger("ScheduleManager")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.setLevel(logging.INFO)

class ScheduleManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ScheduleManager._instance is not None:
            raise RuntimeError("Use get_instance() instead of direct constructor")
        self.tasks: List[Task] = []
        self.observers = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = ScheduleManager()
        return cls._instance

    def register_observer(self, obs):
        self.observers.append(obs)

    def _notify(self, msg: str):
        for o in self.observers:
            try:
                o.notify(msg)
            except Exception:
                logger.exception("Observer failed")

    def add_task(self, task: Task):
        for existing in self.tasks:
            if existing.overlaps(task):
                msg = f"Task '{task.name}' conflicts with '{existing.name}'"
                self._notify(msg)
                raise ValueError(msg)
        self.tasks.append(task)
        self.tasks.sort(key=lambda t: t.start)
        logger.info(f"Task added: {task.name}")

    def remove_task(self, name: str):
        for i, t in enumerate(self.tasks):
            if t.name == name:
                self.tasks.pop(i)
                logger.info(f"Removed {name}")
                return
        raise ValueError("Task not found")

    def mark_complete(self, name: str):
        for t in self.tasks:
            if t.name == name:
                t.completed = True
                logger.info(f"Completed {name}")
                return
        raise ValueError("Task not found")

    def view_tasks(self) -> List[Task]:
        return list(self.tasks)

    def clear_all(self):
        self.tasks.clear()
        logger.info("All tasks cleared")
