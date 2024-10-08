from flask import Flask
from flask import request
import socket
from datetime import datetime
import requests
import time
import os
# If __version__.py is in the same package as this script
from __version__ import __version__
current_version = __version__

print(f"The current version of the package is: {current_version}")

app = Flask(__name__)
GLOBAL_lIST = []

MASTER_VERSION = current_version

CUSTOM_EVENT = {
        "eventType": "Google-Cloud-Event-MachineEvent",
        "summary": "Capture a Log Event from GKE. This is demonstration",
        "severity": "warning",
        "scope": {
            "clusters": ["autopilot-cluster-2"],
            "serviceNames": ["frontend"],
            "namespaces": ["frontend"]
        },
        "details": {
            "hostname": "server-333332ww",
            "ipaddress": "192.169.1.1",
            "Owner": "Hugh Brien",
            "Email": "hugh@hughbrien.com",
            "timestamp": "Tue, 06 Jun 2023 18:54:58 GMT",
            "url": "http://34.172.104.248:5000/webhook",
            "cluster_id": "autopilot-cluster-2",
            "container_name": "frontend",
            "location": "us-central1",
            "namespace_name": "frontend",
            "pod_name": "frontend-885b7ff57-mdfg",
            "project_id":"hpb-bank-of-anthos"
        }
}

TEST_EVENT = {
  "handler": "frontend",
  "incident": {
    "condition": {
      "conditionMatchedLog": {
        "filter": "\"GET /version HTTP/1.1\"",
        "resourceContainers": [
          "projects/hpb-bank-of-anthos"
        ]
      },
      "displayName": "Log match condition",
      "name": "projects/hpb-bank-of-anthos/alertPolicies/10224692307253098708/conditions/10224692307253099895"
    },
    "condition_name": "Log match condition",
    "documentation": {
      "content": "Get Version Alert",
      "mime_type": "text/markdown"
    },
    "ended_at": "null",
    "incident_id": "0.mybdstmr76pg",
    "metadata": {
      "system_labels": {},
      "user_labels": {}
    },
    "metric": {
      "displayName": "",
      "labels": {},
      "type": ""
    },
    "policy_name": "Get Version Alert",
    "resource": {
      "labels": {
        "cluster_name": "autopilot-cluster-2",
        "container_name": "frontend",
        "location": "us-central1",
        "namespace_name": "frontend",
        "pod_name": "frontend-885b7ff57-mdfgp",
        "project_id": "hpb-bank-of-anthos"
      },
      "type": "k8s_container"
    },
    "resource_id": "",
    "resource_name": "Kubernetes Container labels {cluster_name=autopilot-cluster-2, container_name=frontend, location=us-central1, namespace_name=frontend, pod_name=frontend-885b7ff57-mdfgp, project_id=hpb-bank-of-anthos}",
    "resource_type_display_name": "Kubernetes Container",
    "scoping_project_id": "hpb-bank-of-anthos",
    "scoping_project_number": 301868641236,
    "started_at": 1686076691,
    "state": "open",
    "summary": "Log match condition fired for Kubernetes Container with {cluster_name=autopilot-cluster-2, container_name=frontend, location=us-central1, namespace_name=frontend, pod_name=frontend-885b7ff57-mdfgp, project_id=hpb-bank-of-anthos}.",
    "url": "https://console.cloud.google.com/monitoring/alerting/incidents/0.mybdstmr76pg?project=hpb-bank-of-anthos"
  },
  "timestamp": "Tue, 06 Jun 2023 18:54:58 GMT",
  "url": "http://34.172.104.248:5000/webhook",
  "version": "1.2"
}




@app.route('/webhook',  methods=['GET','POST'])
def webhook():  # put changes here
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        json["timestamp"] = datetime.now()
        json["handler"] = "frontend"
        json["url"] = "http://34.172.104.248:5000/webhook"
        print(type(json))
        GLOBAL_lIST.append(json)
        return json
    else:
        return 'Content-Type is not supported!.  Only POST is available on Webhook'

@app.route('/lastrequest',  methods=['GET'])
def lastrequest():  # put application's code here
    content_type = request.headers.get('Content-Type')
    return GLOBAL_lIST[-1]

@app.route('/version',  methods=['GET'])
def version():  # put application's code here
    hostname = socket.gethostname()
    headers = {'content-type': 'application/json'}
    json = {}
    json["timestamp"] =  datetime.now()
    json["version"] = MASTER_VERSION
    json["service_name"] = "frontend"
    json['hostname'] = str(hostname)
    json["author"] = "hughpbrien"
    print(json)
    return json

@app.route('/translate',  methods=['GET'])
def translate():  # put application's code here
    headers = {'content-type': 'application/json'}
    json = TEST_EVENT
    print(json)
    return json

@app.route('/', methods=['GET'])
def welcome_message_json():  # put application's code here
    hostname = socket.gethostname()
    return '{"message":"Welcome to the Kubernetes Demo Everyone ",' \
           '"hostname":"' + hostname + '",' \
           '"name":"Hugh Brien",' \
           '"email":"hugh@komodor.com - broken"}'

@app.route('/machine', methods=['GET'])
def machine_event():  # put application's code here
    new_socket = socket
    hostname = socket.gethostname()
    return '{"type":"machine event",' \
           '"hostname":"' + hostname + '",' \
            '"cluster":"super-k8s-cluster",' \
            '"namespace":"frontend",' \
           '"owner":"hugh@komodor.com"}'

@app.route('/healthz/live')
def live():  # liveness
    return '{"status":"live"}'

@app.route('/healthz/ready')
def ready():  # readyness
    return '{"status":"ready"}'

@app.route('/send_event')
def send_event():
    custom_event = {
        "eventType": "Google Cloud Event",
        "summary": "Host Change Events",
        "severity": "error",
        "scope": {
            "clusters": ["hpbx-mac-cluster"],
            "serviceNames": ["frontend"],
            "namespaces": ["frontend"]
        },
        "details": {
            "hostname": "server-333332ww",
            "ipaddress": "192.169.1.1",
            "Owner": "Hugh Brien",
            "Email": "hugh@hughbrien.com"
        }
    }
    posting = requests.post("http://frontend.frontend.svc.cluster.local:5000/webhook",
                            json=custom_event,
                            headers={"Content-Type":"application/json",
                                     "x-api-key":"demo-key"})
    print(posting)
    status_code = str(posting.ok)
    result = {"http_return_code" : posting.status_code,
              "http_status": status_code }
    return result


@app.route('/get_catalog_version')
def get_service_version():
    hostname = socket.gethostname()
    posting = requests.get("http://catalog.commerce.svc.cluster.local:5000/version",
                            headers={"Content-Type":"application/json",
                                         "x-api-key":"21527fbe-3fda-4080-b3ec-931a81a361ba"})
    print(posting)
    status_code = str(posting.ok)
    posting.content
    result = {"http_return_code" : posting.status_code,
              "hostname": "catalog",
              "http_status": status_code }
    result = posting.content
    return result

@app.route('/get_shipping_version')
def get_shipping_version():
    posting = requests.get("http://shipping.commerce.svc.cluster.local:5000/version",
                            headers={"Content-Type":"application/json",
                                     "x-api-key":"21527fbe-3fda-4080-b3ec-931a81a361ba"})
    print(posting)
    status_code = str(posting.ok)
    hostname = socket.gethostname()

    result = {"http_return_code" : posting.status_code,
              "hostname": "shipping",
              "http_status": status_code }
    return result




if __name__ == '__main__':
    app.run()
