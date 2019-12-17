import requests

payload = {'eid': '', '': '', 'limit': '', 'address': "", 'start_time': ''}
r = requests.post('http://127.0.0.1:8000/api/add_event/', data=payload)
print(r.json())
print(r.status_code)

