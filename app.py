from flask import Flask
#import json
#import jsonify
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    hostname = socket.gethostname()
    return '<h1>Hello World ' + hostname + '!!!</h1><h2>Author Hugh Brien</h2>'

@app.route('/data')
def get_data():  # put application's code here
    return 'Data is Comming '

@app.route('/service',  methods=['GET'])
def service():  # put application's code here
    service_result = {
        "name": "frontend",
        "owner":"Hugh Brien",
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

