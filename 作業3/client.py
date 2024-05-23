##client.py is for to get/post information into the server

import requests

url = 'http://127.0.0.1:5000'
path = '/device/status'
api_key = 'ZV57oAEStAZltOBBW4NtaC6QdSDPCdG1'

def get_user_input():
    user_input = input('Input command(set/get): ')
    return user_input.split()

def get_device_status():
    headers = {
        'Api-Key': api_key
    }
    return requests.get(url + path, headers=headers)

def set_device_status(status):
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': api_key
    }
    payload = {
        'status': status
    }
    return requests.post(url + path, headers=headers, json=payload)

while True:
    try:
        inputs = get_user_input()

        if inputs[0] == 'get':
            response = get_device_status()
            print(response.text)
        elif inputs[0] == 'set':
            if len(inputs) > 1:
                status = inputs[1]
                response = set_device_status(status)
                print(response.text)
            else:
                print('No status provided')
    except:
        continue