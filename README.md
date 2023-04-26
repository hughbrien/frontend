# Komodor Frontend Service Demonstration
Frontend in Python

The Project was created to demonstrate and exeplify the Integration between [Git](https://git-scm.com/) based source control and [Komodor](http://www.komodor.com)

### PreRequisites 

- ***Fork this Project*** - GitHub Repository
- You will need Commit and Push privledges on your Source code repository
- Ensure you are have access to an appropriate docker runtime
- Push Access to a Docker Image  **Repository**. I am usign {DockerHub}(https://hub.docker.com/repository/docker/hughbrien/frontend/general)


## Overview of Steps 

- Clone the Repository
- ```git clone https://github.com/hughbrien/frontend ```
- Make changes to the Source Code 
- Commit and Push the Changes to the Source code
- Retrieve the Github Hash from the Commit
- Update the [Frontend Deployment Manifest]() with the Github Hash from the Commit
- Build and Push the Deployment to a PUBLIC/Private Repository 
- ```docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:2.0.1 .```
- ``` k apply -f frontend.yaml         ```
- Commit change to Frontend manifest yaml.
- Update/Confirm  your Deployment manifest has the correct Ropository Image reference

## Need a link to the Services 

```kuberctl get service -n frontend``` will return the PUBLIC IPADDRESS 

- [Frontend Actual](http://34.173.139.195:5000/)


## View Changes in Komodor 
- [Frontend Service](https://app.komodor.com/services/demo.google-se-cluster-frontend.frontend)

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

