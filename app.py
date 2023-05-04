from flask import Flask
#import json
#import jsonify
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def welcome_message_json():  # put application's code here
    hostname = socket.gethostname()
    return '{"message":"Welcome to Everyone",' \
           '"hostname":"' + hostname + '",' \
           '"name":"Hugh Brien",' \
           '"email":"hugh@komodor.com"}'

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

@app.route('/basic',  methods=['GET'])
def basic():  # put application's code here
    service_result = {
        "name": "basic",
        "owner":"Demo Basic",
        "description":"The Basic Demo is Great"
    }
    return service_result

@app.route('/ready',  methods=['GET'])
def readiness():  # put application's code here
    service_result = {
        "name": "frontend",
        "status":"ready",
        "description":"The frontend service is Ready"
    }
    return service_result
@app.route('/live',  methods=['GET'])
def liveness():  # put application's code here
    service_result = {
        "name": "frontend",
        "status":"live",
        "description":"The Frontend Service is Live"
    }
    return service_result


if __name__ == '__main__':
    app.run()

