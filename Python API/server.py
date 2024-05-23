from flask import request
from flask import jsonify
from flask import Flask

#this is where we setup the server

app = Flask(__name__)

success_message = {'message': 'SUCCESS'}
unauthorized_message = {'message': 'UNAUTHORIZED'}

api_key = 'ZV57oAEStAZltOBBW4NtaC6QdSDPCdG1'

global status
status = 'off'

@app.route('/device/status', methods=['GET'])
def get_device_status():
    if request.headers.get('Api-Key') != api_key:
        return jsonify(unauthorized_message)

    return jsonify({'status': status})

@app.route('/device/status', methods=['POST'])
def set_device_status():
    if request.headers.get('Api-Key') != api_key:
        return jsonify(unauthorized_message)

    data = request.get_json()
    if data['status']:
        global status
        status = data['status']

    return jsonify(success_message)

if __name__ == '__main__':
    app.run(debug=True)