curl localhost:5000/jobs -d '{"start": "1", "end": "2"}' -H 'Content-Type: application/json'


docker-compose up -d


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


## Kubernetes Teardown

To close all the pods, run:

```
homework07]$ kubectl delete -f deploy/api && \
  kubectl delete -f deploy/db && \
  kubectl delete -f deploy/debug && \
  kubectl delete -f deploy/worker
```
