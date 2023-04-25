# frontend
Frontend in Python

- Ensure you are access to the appropriate docker runtime
- You also need to access to a Repository. Updates


## Changes in Komodor 

- Make changes to the Source Code 
- Commit and Push the Changes
- Build and Push the Deployment to a PUBLIC/Private Repository 
- Update/Confirm  your Deployment manifest has the correct Ropository Image reference



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

## View Changes in Komodor 
- [Frontend Service](https://app.komodor.com/services/demo.google-se-cluster-frontend.frontend)
