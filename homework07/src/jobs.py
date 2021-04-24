"""Utilities for creating and managing jobs."""

import uuid

from hotqueue import HotQueue
import redis

rd = redis.StrictRedis(
    host="redis", port=6379, db=0, charset="utf=8", decode_responses=True
)
q = HotQueue("queue", host="redis", port=6379, db=1)


def _generate_jid():
    return str(uuid.uuid4())


def _generate_job_key(jid: str) -> str:
    return f"job.{jid}"


def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {"id": jid, "status": status, "start": start, "end": end}
    return {
        "id": jid.decode("utf-8"),
        "status": status.decode("utf-8"),
        "start": start.decode("utf-8"),
        "end": end.decode("utf-8"),
    }


def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    # update call to save_job:
    _save_job(_generate_job_key(jid), job_dict)
    # update call to queue_job:
    _queue_job(jid)
    return job_dict


def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)


def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)


def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(
        _generate_job_key(jid), "id", "status", "start", "end"
    )
    job = _instantiate_job(jid, status, start, end)
    if job:
        job["status"] = new_status
        _save_job(_generate_job_key(job["id"]), job)
    else:
        raise Exception()


def get_job_status(jid: str) -> str:
    return rd.hgetall(f"job.{jid}")
