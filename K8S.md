
# Kubernetes Local 

## install and run metrics-server 

```shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

```

```yaml 

    spec:
      containers:
          args:
            - '--kubelet-insecure-tls'
- 
```

```yaml
Change ClusterIP to LoadBalancer
spec:
  type: LoadBalancer
```
### Run the Commnands 
```shell
kubectl top pods -A
kubectl top nodes -A

```