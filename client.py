import requests

# Checking values
custom_event = {
  "eventType": "Google Cloud Event",
  "summary": "Host Change Events",
  "severity": "error",
  "scope": {
    "clusters":["autopilot-cluster-2"],
    "serviceNames":["frontend"],
    "namespaces":["frontend"]
  },
  "details": {
    "hostname": "server-333332ww",
    "ipaddress": "192.169.1.1",
    "Owner": "Hugh Brien",
    "Email": "hugh@hughbrien.com"
  }
}
posting =requests.post("https://api.komodor.com/mgmt/v1/events",
              json=custom_event,
              headers={"Content-Type":"application/json",
                        "x-api-key":"21527fbe-3fda-4080-b3ec-931a81a361ba"})

print(posting)


