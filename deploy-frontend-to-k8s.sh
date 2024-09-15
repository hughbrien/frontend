#!/bin/bash

# Function definitions
function deploy() {
    echo "Deploying Frontend Service..."
    kubectl apply -f ./manifests/frontend-namespace.yaml
    kubectl apply -f ./manifests/frontend-config-map.yaml
    kubectl apply -f ./manifests/frontend.yaml
    kubectl apply -f ./manifests/frontend-service.yaml
}

function undeploy() {
    echo "Deleting the Frontend Deployment..."
    kubectl delete ns frontend
}

# Check if a parameter is provided
if [ -z "$1" ]; then
    echo "Error: No parameter provided. Usage: ./deploy-frontend-to-k8s.sh {deploy|undeploy}"
    exit 1
fi

# Execute a function based on the parameter value
case $1 in
    deploy)
        deploy
        ;;
    undeploy)
        undeploy
        ;;
    *)
        echo "Invalid option. Usage: ./run_function.sh {deploy|undeploy}"
        exit 1
        ;;
esac
