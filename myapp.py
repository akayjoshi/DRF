# this file is used for make a request to out create view with post request make sure requests package is installed
import requests
import json 

url = 'http://127.0.0.1:8000/create/'

data = {
        'name': 'kiran',
        'roll': 3,
        'city': 'sri dunagargarh'
}

json_data = json.dumps(data)

r = requests.post(url = url, data = json_data)

data = r.json()

print(data)