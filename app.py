from flask import Flask
from flask import request
import socket
from datetime import datetime


app = Flask(__name__)

GLOBAL_lIST = []
SERVICE_VERSION = "2.0.9"

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
    headers = {'content-type': 'application/json'}
    json = {}
    json["timestamp"] =  datetime.now()
    json["version"] = SERVICE_VERSION
    json["service_name"] = "frontend"
    json["author"] = "hughpbrien"
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


if __name__ == '__main__':
    app.run()

