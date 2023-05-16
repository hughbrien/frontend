curl --header "Content-Type: application/json" --header "x-api-key:XXXXXXXXXXXXXXXX" \
  --request POST \
  --data '{"Message":"Decreased Resources", "CPU" : "1", "Memory":"2GB"}' "https://api.komodor.com/v0/config_change?clusterName=google-se-cluster&namespace=frontend&serviceName=frontend"
