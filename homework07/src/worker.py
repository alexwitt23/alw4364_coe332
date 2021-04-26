import time
import os

import hotqueue

import jobs

_WORKER_IP = os.environ.get("WORKER_IP", "0.0.0.0")


@jobs.q.worker
def execute_job(jid: str) -> None:
    jobs.update_job_status(jid, "in progress")
    jobs.add_job_data(jid, {"worker-ip": _WORKER_IP})
    time.sleep(15)
    jobs.update_job_status(jid, "complete")


if __name__ == "__main__":
    execute_job()
