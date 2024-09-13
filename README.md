# Branch harness-first

# frontend
Frontend in Python / Changes for the Demo / Fixed the Bug

- Ensure you are have access to an  appropriate docker runtime/envioronment such as ***Docker Desktop*** [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- [Fork](https://github.com/hughbrien/frontend/fork)  this Repository 
- You also need the following
- Cluster Authentication
- Read / Write Access to the  Repository
- Read / Write Git Repository 


## API
- @app.route('/webhook',  methods=['GET','POST'])
- @app.route('/lastrequest',  methods=['GET'])
- @app.route('/version',  methods=['GET'])
- @app.route('/healthz/live')
- @app.route('/healthz/ready')


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

Clone this repository
```
git clone https://github.com/hughbrien/frontend
cd frontend
```

### Docker.io
```

docker buildx build --platform linux/amd64,linux/arm64 --push -t hughbrien/frontend:X.X.X .

```

### JFrog 
```
export VERSION=2.1.10
docker buildx build --platform linux/amd64,linux/arm64 --push -t hugenet.jfrog.io/docker/frontend:2.1.10 .
docker pull hugenet.jfrog.io/docker/hello-world:latest

```

## Deployment
```
kubectl create ns frontend 
kubectl apply -f ./manifests/

```



## Rollout 
```
export VERSION=X.X.X
kubectl set image deployment/frontend frontend=frontend:X.X.X -n frontend
kubectl rollout restart deployment/frontend 
```


## Need a link to the Services 

```kuberctl get service -n frontend``` will return the PUBLIC IPADDRESS 

- [Frontend Actual](http://34.173.139.195:5000/)


## From the Beginning Each Step. 
So you run your service local. This is very python developer/specific 

```git clone https://github.com/hughbrien/frontend ```

Make changes to the app.py, Dockerfile, README.md 


```kubectl apply -f frontend.yaml```

### Dealing with secrets 

```
echo -n 'S!B\*d$zDsb=' > ./password.txt

kubectl create secret generic db-user-pass --from-file=./password.txt
```

View the contents of the Secret you created:
```
kubectl get secret db-user-pass -o jsonpath='{.data}'
```
The output is similar to:
```
{ "password": "UyFCXCpkJHpEc2I9"}
```
Decode the password data:

echo 'UyFCXCpkJHpEc2I9' | base64 --decode
The output is similar to:
S!B\*d$zDsb=

### Create ArgoCD Entry 

argocd app create frontend  --repo `git config --get remote.origin.url` --path manifests --dest-server https://kubernetes.default.svc --dest-namespace frontend

### Port Forward for Service
kubectl port-forward -n frontend  service/frontend 5000:5000

kubectl port-forward -n frontend  service/frontend 5000:5000


