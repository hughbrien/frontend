from flask import Flask
from flask import request

#import json
#import jsonify
import socket
import datetime

app = Flask(__name__)


@app.route('/webhook',  methods=['GET','POST'])
def webhook():  # put application's code here
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        json["timestamp"] = datetime.datetime.now()
        json["handler"] = "frontend"
        json["url"] = "http://34.172.104.248:5000/webhook"
        print(type(json))
        return json
    else:
        return 'Content-Type not supported!'


@app.route('/')
def welcome_message_json():  # put application's code here
    hostname = socket.gethostname()
    return '{"message":"Welcome to the Kubernetes Demo Everyone ",' \
           '"hostname":"' + hostname + '",' \
           '"name":"Hugh Brien",' \
           '"email":"hugh@komodor.com - broken"}'


@app.route('/healthz/live')
def live():  # liveness
    return '{"status":"live"}'

@app.route('/healthz/ready')
def ready():  # readyness
    return '{"status":"ready"}'

@app.route('/data')
def get_data():  # put application's code here
    return 'Data is Coming '

@app.route('/service',  methods=['GET'])
def service():  # put application's code here
    service_result = {
        "name": "frontend",
        "owner":"Hugh Brien",
        "phone":"5551212",
        "email":"hugh@komodor.com",
        "description":"The HTTP service to catch all incoming data"
    }
    return service_result

if __name__ == '__main__':
    app.run()

