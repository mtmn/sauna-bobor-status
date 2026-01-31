from threading import Thread
from typing import Callable
from loguru import logger
import time


class TaskState:
    interval: float
    func: Callable[[], None]
    last_run: float

    def __init__(self, interval: float, func: Callable[[], None]):
        self.interval = interval
        self.func = func
        self.last_run = 0.0


class Scheduler:
    def __init__(self):
        self.tasks: list[TaskState] = []
        self._running: bool = False
        self._thread: Thread | None = None

    def add_task(self, interval: float, func: Callable[[], None]) -> None:
        """Add a task to be executed every `interval` seconds."""
        self.tasks.append(TaskState(interval, func))
        logger.info(f"Registered task {func.__name__} to run every {interval}s")

    def _run_loop(self) -> None:
        while self._running:
            now = time.time()
            for task in self.tasks:
                if now - task.last_run >= task.interval:
                    try:
                        task.func()
                    except Exception as e:
                        logger.error(f"Error in task {task.func.__name__}: {e}")
                    task.last_run = now

            # Prevent busy waiting
            time.sleep(0.1)

    def start(self) -> None:
        """Start the scheduler in a background thread."""
        if self._running:
            return

        self._running = True
        self._thread = Thread(target=self._run_loop, daemon=True)
        self._thread.start()
