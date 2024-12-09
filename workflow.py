from typing import Any, Optional
from abc import ABC, abstractmethod

from .job import Job

from utils.logger import setup_logger

logger = setup_logger(__name__)

class Workflow(ABC):
    def __init__(self, shared_vars: Any):
        self.shared_vars: Any = shared_vars
        self.jobs: list[Job] = []

    # TODO: self.jobs 에 job 을 추가합니다.
    def add_job(self, job: Job):
        logger.debug(f'{job.name} 추가합니다.')
        self.jobs.append(job)

    def get_job(self):
        return self.jobs
    
    def run(self):
        roojob: Job = None
        prejob: Job = None
        for job in self.jobs:
            if prejob == None:
                rootjob = job
                prejob = job
            else:
                prejob.set_next(job)
        
        rootjob.exec_job({"YYYYMM":"202401"})




if __name__ == "__main__":

    class MonkeyJob(Job):  
        def task(self, shared_vars: Any) -> None:
            # TODO:

            print(f"Monkey {self.local_vars['YYYYMM']} Job {shared_vars['YYYYMM']}")

    class CatJob(Job):
        def task(self, shared_vars: Any) -> None:
            # TODO:

            print(f"Cat {self.local_vars['YYYYMM']} Job {shared_vars['YYYYMM']}")

    class DogJob(Job):
        def task(self, shared_vars: Any) -> None:
            # TODO:

            print(f"Dog {self.local_vars['YYYYMM']} Job {shared_vars['YYYYMM']}")

    monkey = MonkeyJob({"YYYYMM":"202101"}, name="monkey job")
    cat = CatJob({"YYYYMM":"202201"}, name="cat job")
    dog = DogJob({"YYYYMM":"202301"}, name="dog job")

    monkey.set_next(cat).set_next(dog)

    print("start")

    monkey.exec_job({"YYYYMM":"202401"})

    cat.exec_job({"YYYYMM":"202402"})

    print('end')

    print('workflow start')

    wf = Workflow({"YYYYMM":"202401"})
    wf.add_job(monkey)
    wf.add_job(cat)
    wf.add_job(dog)

    wf.run()

    print('workflow end')


    




