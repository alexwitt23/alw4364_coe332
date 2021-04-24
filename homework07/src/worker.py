import time

import hotqueue

import jobs

q = hotqueue.HotQueue("queue", host="0.0.0.0", port=6379, db=2)


@q.worker
def execute_job(jid: str) -> None:
    jobs.update_job_status(jid, "in progress")
    time.sleep(15)
    jobs.update_job_status(jid, "complete")


if __name__ == "__main__":
    execute_job()
