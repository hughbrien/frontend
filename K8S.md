
# Kubernetes Local 

## install and run metrics-server 

```shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

```

### Update the Deployment manifest 
```yaml
    spec:
      containers:
          args:
            - '--kubelet-insecure-tls' 
```

### Change ClusterIP to LoadBalancer in the metrics-server Kubernetes Service manifest

```yaml
spec:
  type: LoadBalancer
```

### Run the Commnands 
```shell
kubectl top pods -A
kubectl top nodes -A

```