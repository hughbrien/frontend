from flask import Flask
import json
import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


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

