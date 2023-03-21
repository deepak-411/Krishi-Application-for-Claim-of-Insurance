import requests

url = 'http://localhost:5000/get_data'
r = requests.post(url,json={'district': 'MOTIHARI','state':'BIHAR'})
print(r.json())