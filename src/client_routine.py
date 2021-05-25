# importing the requests library
import requests
from requests.auth import HTTPBasicAuth
import time

is_inproduction = False


base_path = "http://ip172-18-0-38-c2m622lmrepg008vkg7g-80.direct.labs.play-with-docker.com/"
base_localpath = "http://localhost:80/"
URL = ''
if is_inproduction == True:
    URL = base_path
else:
    URL = base_localpath

# login and get token
payload = {'username': 'user', 'password': 'password'}
r = requests.get(url = URL + 'login', auth = HTTPBasicAuth('user', 'password'))

data  = r.json()
token = data['token']
print('Auth token: ',token)
print()


## get employees list

r = requests.get(url = URL + 'employees/', headers = {"Authorization":"Bearer " + token} )

data  = r.json()
print('Employee list:')
print(data)
print()

# post data at the Database
employee_array = [{
"id": "1",
"name": "Anakin Skywalker",
"email": "skywalker@ssys.com.br",
"department": "Architecture",
"salary": "4000.00",
"birth_date": "01-01-1983"},
{
"id": "2",
"name": "Obi-Wan Kenobi",
"email": "kenobi@ssys.com.br",
"department": "Back-End",
"salary": "3000.00",
"birth_date": "01-01-1977"},
{
