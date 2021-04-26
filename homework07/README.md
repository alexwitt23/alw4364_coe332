
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

## Part B

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
