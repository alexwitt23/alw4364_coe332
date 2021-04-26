
## API

Here are the endpoints present in the API.


#### Jobs

Add new job to the database.

* URL: /jobs
* Method: `POST`
* URL Params
  - None
* Data Params
  - {"start": "1", "end": "2"}


#### Job Status

Returns job status.

* URL: /jobs_status
* Method: `GET`
* URL Params
  - job_id=[string]
* Data Params
  - None


#### Completed Jobs

Returns all completed jobs.

* URL: /completed_jobs
* Method: `GET`
* URL Params
  - None
* Data Params
  - None


#### Incomplete Jobs

Returns all incomplete jobs.

* URL: /incomplete_jobs
* Method: `GET`
* URL Params
  - None
* Data Params
  - None


#### Inprogress Jobs

Returns all inprogress jobs.

* URL: /inprogress_jobs
* Method: `GET`
* URL Params
  - None
* Data Params
  - None



## Kubernetes

Start up all the services and pods:

```
homework07]$ kubectl apply -f deploy/api && \
  kubectl apply -f deploy/db && \
  kubectl apply -f deploy/debug && \
  kubectl apply -f deploy/worker
```

The first time the services are started, you'll need to grab the IP address of
the redis service and add that to the api and worker .ymls:

```
$ kubectl get service
NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
alexwitt-hw7-redis-service    ClusterIP   10.102.15.202    <none>        6379/TCP         2m59s
```

Add this `CLUSTER-IP` to the ymls:

```
env:
  - name: REDIS_IP
    value: "10.102.15.202"
```

then apply the changes:

```
homework07]$ kubectl apply -f deploy/api && \
  kubectl apply -f deploy/worker
```


## Usage

Find the python debug container:

```
$ kubectl get pods
NAME                                             READY   STATUS    RESTARTS   AGE
alexwitt-hw7-debug-5cc8cdd65f-8n8j4              1/1     Running   0          10m
alexwitt-hw7-flask-deployment-c5ddc9bd8-g4mfb    1/1     Running   0          8m12s
alexwitt-hw7-flask-deployment-c5ddc9bd8-kkqpn    1/1     Running   0          8m13s
alexwitt-hw7-redis-deployment-547dc86c4f-726mt   1/1     Running   0          10m
alexwitt-hw7-worker-deployment-65f47f469-gfml8   1/1     Running   0          8m13s
alexwitt-hw7-worker-deployment-65f47f469-kt278   1/1     Running   0          8m11s
```

Then, exec into the pod so we can access the kubernetes network:
```
kubectl exec -ti alexwitt-hw7-debug-5cc8cdd65f-8n8j4 -- /bin/bash
```


Inside the pod, we can issue POST commands to the flask API:

```
# curl 10.109.215.82:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'
```

This command will return the job description:

```
{
  "end": "2",
  "id": "7c3d047d-efc0-4672-b1bd-9f981e31337b",
  "start": "1",
  "status": "submitted"
}
```

In the debug pod, you can now look into the redis database and check the job's status:

```
root@alexwitt-hw7-debug-5cc8cdd65f-8n8j4:/# python3
Python 3.9.2 (default, Feb 19 2021, 17:11:58)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis; import hotqueue
>>> rd = redis.StrictRedis(host="10.103.175.2", port=6379, db=0, charset="utf=8", decode_responses=True)
>>> rd.hgetall('job.7c3d047d-efc0-4672-b1bd-9f981e31337b')
{'id': '7c3d047d-efc0-4672-b1bd-9f981e31337b', 'status': 'complete', 'start': '1', 'end': '2'}
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


## Part A

1. See `Dockerfile`
2. See:
  * `deploy/api/alexwitt-hw7-flask-deployment.yml`
  * `deploy/worker/alexwitt-hw7-worker-deployment.yml`
3. Create some jobs
  a.
    ```
    root@alexwitt-hw7-debug-5cc8cdd65f-8n8j4:/# curl 10.109.215.82:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'; \
      curl 10.109.215.82:5000/jobs -d '{"start": "3", "end": "4"}' -H 'Content-Type: application/json'; \
      curl 10.109.215.82:5000/jobs -d '{"start": "5", "end": "6"}' -H 'Content-Type: application/json'; \
      curl 10.109.215.82:5000/jobs -d '{"start": "7", "end": "8"}' -H 'Content-Type: application/json'; \
      curl 10.109.215.82:5000/jobs -d '{"start": "9", "end": "10"}' -H 'Content-Type: application/json';
    ```

    which outputs the job data:

    ```
    {
      "end": "2",
      "id": "81e4d5ac-9fd8-410b-8e98-e60afb94b9bf",
      "start": "1",
      "status": "submitted"
    }
    {
      "end": "4",
      "id": "822b7238-78ea-4622-9097-ffc62703d816",
      "start": "3",
      "status": "submitted"
    }
    {
      "end": "6",
      "id": "ac76a47a-ef25-4969-8e0e-b614f1124b26",
      "start": "5",
      "status": "submitted"
    }
    {
      "end": "8",
      "id": "8710819b-db76-4116-8ed7-3ea9e6388928",
      "start": "7",
      "status": "submitted"
    }
    {
      "end": "10",
      "id": "47c22e9b-a512-4820-9a1a-c03c07569a73",
      "start": "9",
      "status": "submitted"
    }
    ```

  b. The job status can be checked by entering a python debug pod and manually checking
     the redis database:


    root@alexwitt-hw7-debug-5cc8cdd65f-8n8j4:/# python3
    Python 3.9.2 (default, Feb 19 2021, 17:11:58)
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import redis; import hotqueue
    >>> rd = redis.StrictRedis(host="10.103.175.2", port=6379, db=0, charset="utf=8", decode_responses=True)
    >>> rd.hgetall('job.81e4d5ac-9fd8-410b-8e98-e60afb94b9bf')
    {'id': '81e4d5ac-9fd8-410b-8e98-e60afb94b9bf', 'status': 'complete', 'start': '1', 'end': '2'}
    >>> rd.hgetall('job.822b7238-78ea-4622-9097-ffc62703d816')
    {'id': '822b7238-78ea-4622-9097-ffc62703d816', 'status': 'complete', 'start': '3', 'end': '4'}
    >>> rd.hgetall('job.ac76a47a-ef25-4969-8e0e-b614f1124b26')
    {'id': 'ac76a47a-ef25-4969-8e0e-b614f1124b26', 'status': 'complete', 'start': '5', 'end': '6'}
    >>> rd.hgetall('job.8710819b-db76-4116-8ed7-3ea9e6388928')
    {'id': '8710819b-db76-4116-8ed7-3ea9e6388928', 'status': 'complete', 'start': '7', 'end': '8'}
    >>> rd.hgetall('job.47c22e9b-a512-4820-9a1a-c03c07569a73')
    {'id': '47c22e9b-a512-4820-9a1a-c03c07569a73', 'status': 'complete', 'start': '9', 'end': '10'}



## Part B

1. See `deploy/worker/alexwitt-hw7-worker-deployment.yml`
2. A new function is created in `src.jobs.py` to update a job's content. This is called
  by the worker function.

## Part C

Worker scaled to 2 pods:

```
spec:
  replicas: 2
```

Create 10 more jobs:

```
root@alexwitt-hw7-debug-5cc8cdd65f-8n8j4:/# curl 10.109.215.82:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "3", "end": "4"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "5", "end": "6"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "7", "end": "8"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "9", "end": "10"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "11", "end": "12"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "13", "end": "14"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "15", "end": "16"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "17", "end": "18"}' -H 'Content-Type: application/json'; \
  curl 10.109.215.82:5000/jobs -d '{"start": "19", "end": "20"}' -H 'Content-Type: application/json';
```

  b.
  ```
  root@alexwitt-hw7-debug-5cc8cdd65f-8n8j4:/# python3
      Python 3.9.2 (default, Feb 19 2021, 17:11:58)
      [GCC 8.3.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import redis; import hotqueue
      >>> rd = redis.StrictRedis(host="10.103.175.2", port=6379, db=0, charset="utf=8", decode_responses=True)
      >>> for id in ids:
      ...     rd.hgetall(f'job.{id}')
      ...
      {'id': 'f56fd601-6d21-410b-9beb-04d88bdb7daa', 'status': 'complete', 'start': '1', 'end': '2', 'worker-ip': '10.244.12.150'}
      {'id': 'cea9b8b9-dfe4-4b07-be30-b296d9ad5d7d', 'status': 'complete', 'start': '3', 'end': '4', 'worker-ip': '10.244.15.110'}
      {'id': 'e1381999-170f-42ee-a2bb-a19dac4beff0', 'status': 'complete', 'start': '5', 'end': '6', 'worker-ip': '10.244.12.150'}
      {'id': '250d4b61-7c24-4512-99b4-46866c53a981', 'status': 'complete', 'start': '7', 'end': '8', 'worker-ip': '10.244.15.110'}
      {'id': '3b30544f-98a3-407a-a854-8d4f9c1c57e6', 'status': 'complete', 'start': '9', 'end': '10', 'worker-ip': '10.244.12.150'}
      {'id': 'd2eae15b-6a6c-4420-8eb3-b58e8b9d3e11', 'status': 'complete', 'start': '11', 'end': '12', 'worker-ip': '10.244.15.110'}
      {'id': '10c64db3-84ad-45eb-bcbb-fe8f50e4aefc', 'status': 'complete', 'start': '13', 'end': '14', 'worker-ip': '10.244.12.150'}
      {'id': '3168eba5-505c-4f41-ad79-2b9ccc7bcae0', 'status': 'complete', 'start': '15', 'end': '16', 'worker-ip': '10.244.15.110'}
      {'id': '4664ef33-ac58-4f13-8529-dadd1d3a0d6b', 'status': 'complete', 'start': '17', 'end': '18', 'worker-ip': '10.244.12.150'}
      {'id': '39d8243c-1b46-4322-a814-b2247a37bc9b', 'status': 'complete', 'start': '19', 'end': '20', 'worker-ip': '10.244.15.110'}
  ```

  c. Worker with ip `10.244.12.150` processed 5 jobs, and worker with ip `10.244.15.110` processed 5 jobs.


## Kubernetes Teardown

To close all the pods, run:

```
homework07]$ kubectl delete -f deploy/api && \
  kubectl delete -f deploy/db && \
  kubectl delete -f deploy/debug && \
  kubectl delete -f deploy/worker
```



## Local Deployment
curl localhost:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'


docker-compose up -d
