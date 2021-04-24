import time

import hotqueue

import jobs


@jobs.q.worker
def execute_job(jid: str) -> None:
    jobs.update_job_status(jid, "in progress")
    time.sleep(15)
    jobs.update_job_status(jid, "complete")


if __name__ == "__main__":
    execute_job()
