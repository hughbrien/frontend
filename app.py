from flask import Flask
#import json
#import jsonify
import socket


app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    hostname = socket.gethostname()
    return '<h1>Hello World ' + hostname + '!!!</h1>'

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


if __name__ == '__main__':
    app.run()

