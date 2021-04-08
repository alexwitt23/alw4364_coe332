# Homework 05

> Exploring Kubernetes

## Part A

See `k8s-A.yml` for part A.

1. The contents of `k8s-A.yml`:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: hello
  labels:
    greeting: personalized
spec:
  containers:
    - name: hello
      image: ubuntu:18.04
      command: ['sh', '-c', 'echo "Hello, $NAME!" && sleep 3600']
```

To create the pod, run:
```
kubectl apply -f k8s-A.yml
```

2. With a label of `greeting: personalized`, we can query this label two ways:

    a. First, any pod with the label `greeting`:
    `kubectl get pods  --selector "greeting"`

    b. Second, any pod with the label and key pair `greeting: personalized`:
    `kubectl get pods  --selector "greeting=personalized"`

3. To check the pod's logs, run:
```
$ kubectl logs hello
Hello, !
```

4. To delete the pod, run:
```
$ kubectl delete pods hello
pod "hello" deleted
```

## Part B

See `k8s-B.yml` for part B.

1. The contents of `k8s-B.yml`:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: hello
  labels:
    greeting: personalized
spec:
  containers:
    - name: hello
      image: ubuntu:18.04
      command: ['sh', '-c', 'echo "Hello, $NAME!" && sleep 3600']
```

To create the pod, run:
```
kubectl apply -f k8s-B.yml
```

2.
```
$ kubectl logs hello
Hello, Alex!
```

3.
```
$ kubectl delete pods hello
pod "hello" deleted
```

## Part C

1.
```
---
apiVersion: v1
kind: Pod
metadata:
  name: hello
  labels:
    greeting: personalized
spec:
  containers:
    - name: hello
      image: ubuntu:18.04
      command: ['sh', '-c', 'echo "Hello, $NAME from IP $POD_IP!" && sleep 3600']
      env:
        - name: "NAME"
          value: "Alex"
        - name: "POD_IP"
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
```

2.
```
$ kubectl get pods -o wide
NAME                                    READY   STATUS    RESTARTS   AGE     IP             NODE                         NOMINATED NODE   READINESS GATES
hello                                   1/1     Running   0          42s     10.244.3.110   c01                          <none>           <none>
```

3.
```
$ kubectl logs hello
Hello, Alex from IP 10.244.3.110!
```
