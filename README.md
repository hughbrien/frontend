# frontend
Frontend in Python

- Ensure you are access to the appropriate docker runtime
- You also need the following
- Cluster Authentication
- Read / Write Access to the  Repository
- Read / Write Git Repository 




## Changes in Komodor 

- Make changes to the Source Code 
- Commit and Push the Changes to the Source code
- Retrieve the Github Hash from the Commit
- Update the Deployment Manifest with the Github Hash from the Commit
- Build and Push the Deployment to a PUBLIC/Private Repository 
- ```docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:2.0.1 .```
- ``` k apply -f frontend.yaml         ```
- Commit change to Frontend manifest yaml.
- Update/Confirm  your Deployment manifest has the correct Ropository Image reference


## Build the Image and Push 
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

## Need a link to the Services 

```kuberctl get service -n frontend``` will return the PUBLIC IPADDRESS 

- [Frontend Actual](http://34.173.139.195:5000/)


## From the Beginning Each Step. 
So you run your service local. This is very python developer/specific 

```git clone https://github.com/hughbrien/frontend ```

Make changes to the app.py, Dockerfile, README.md 

```docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:2.0.1 .```


```kubectl apply -f frontend.yaml```

