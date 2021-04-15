# Homework06

```
kubectl apply -f alexwitt-test-flask-service.yml
```

```
kubectl apply -f alexwitt-test-redis-service.yml
```

```
kubectl get services
```

```
kubectl apply -f alexwitt-test-flask-deployment.yml && \
kubectl apply -f alexwitt-test-redis-deployment.yml && \
kubectl apply -f alexwitt-test-redis-pvc.yml
```
