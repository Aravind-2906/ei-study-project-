from datetime import datetime
from task import Task

class TaskFactory:
    @staticmethod
    def parse_time(tstr: str):
        """Convert 'HH:MM' string into datetime.time"""
        try:
            return datetime.strptime(tstr.strip(), "%H:%M").time()
        except Exception:
            raise ValueError("Invalid time format, expected HH:MM")

    @staticmethod
    def create(name: str, start_str: str, end_str: str, priority: str) -> Task:
        start = TaskFactory.parse_time(start_str)
        end = TaskFactory.parse_time(end_str)
        if start >= end:
            raise ValueError("Start time must be before end time")
        return Task(name=name.strip(), start=start, end=end, priority=priority.strip())
