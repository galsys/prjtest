from __future__ import annotations
from typing import Any, Optional

from pipeline.job import Job
from pipeline.workflow import Workflow

from utils.logger import setup_logger

logger = setup_logger(__name__)

class MonkeyJob(Job):  
    def task(self, shared_vars: Any) -> None:
        # TODO:

        logger.info(f"Monkey {self.local_vars['YYYYMM']} Job {shared_vars['YYYYMM']}")

class CatJob(Job):
    def task(self, shared_vars: Any) -> None:
        # TODO:

        logger.info(f"Cat {self.local_vars['YYYYMM']} Job {shared_vars['YYYYMM']}")

class DogJob(Job):
    def task(self, shared_vars: Any) -> None:
        # TODO:

        logger.info(f"Dog {self.local_vars['YYYYMM']} Job {shared_vars['YYYYMM']}")
        
if __name__ == "__main__":

    monkey = MonkeyJob({"YYYYMM":"202101"}, name="monkey job")
    cat = CatJob({"YYYYMM":"202201"}, name="cat job")
    dog = DogJob({"YYYYMM":"202301"}, name="dog job")

    logger.info("workflow start.")

    wf = Workflow({"YYYYMM":"202401"})
    wf.add_job(monkey)
    wf.add_job(cat)
    wf.add_job(dog)

    wf.run()
    logger.info("workflow end.")
