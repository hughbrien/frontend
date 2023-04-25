# frontend
Frontend in Python

- Ensure you are access to the appropriate docker runtime
- You also need to access to a Repository. Updates

```
export VERSION=2.0.1
docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:2.0.1 .
```

## Deployment
```
kubectl apply -f ./frontend.yaml

```

## Rollout 
```
export VERSION=2.0.1
kubectl set image deployment/frontend frontend=frontend:2.0.1 -n frontend
kubectl rollout restart deployment/frontend 
```



