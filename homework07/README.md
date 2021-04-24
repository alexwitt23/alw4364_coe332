curl localhost:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'


docker-compose up -d


## Usage

```
$ curl localhost:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'
{
  "end": "2",
  "id": "559237ef-f2cf-4a7e-b717-325dc163525f",
  "start": "1",
  "status": "submitted"
}
```

```
curl localhost:5000/job_status?job_id=559237ef-f2cf-4a7e-b717-325dc163525f
```

```
curl localhost:5000/completed_jobs
```

```
curl localhost:5000/inprogress_jobs
```

```
curl localhost:5000/incomplete_jobs
```
