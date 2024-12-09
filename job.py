from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

from utils.logger import setup_logger

logger = setup_logger(__name__)

class Job(ABC):
    def __init__(self, local_vars: Any, name: str = "", description: str = "") -> None:
        self.local_vars: Any = local_vars
        self._next_handler: Optional[Job] = None
        self.name: str = name
        self.description: str = description

    def set_next(self, handler:Job) -> Job:
        self._next_handler = handler
        return handler

    @abstractmethod
    def task(self, shared_vars: Any) -> None:
        pass

    @property
    def get_name(self) -> str:
        return self.name

    @get_name.setter
    def set_name(self, name: str) -> None:
        self.name = name

    @property
    def get_description(self) -> str:
        return self.description

    @get_description.setter
    def set_description(self, description: str) -> None:
        self.description = description

    def exec_job(self, shared_vars: Any) -> None:
        logger.debug(f"{self.name} job start")
        self.task(shared_vars)

        logger.debug(f"{self.name} job end")
        if self._next_handler:
            self._next_handler.exec_job(shared_vars)