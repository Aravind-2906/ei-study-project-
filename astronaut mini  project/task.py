from dataclasses import dataclass
from datetime import time

@dataclass
class Task:
    name: str
    start: time
    end: time
    priority: str
    completed: bool = False

    def overlaps(self, other: "Task") -> bool:
        """Return True if two tasks overlap in time."""
        return (self.start < other.end) and (other.start < self.end)

    def __str__(self) -> str:
        status = " (Done)" if self.completed else ""
        return f"{self.start.strftime('%H:%M')} - {self.end.strftime('%H:%M')}: {self.name} [{self.priority}]{status}"
