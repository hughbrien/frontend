from flask import Flask
from flask import request

#import json
#import jsonify
import socket
import datetime

app = Flask(__name__)


@app.route('/webhook',  methods=['GET','POST'])
def webhook():  # put application's code here
    data = request.data
    print(data)
    # need posted data here
    service_result = data
    return service_result
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

