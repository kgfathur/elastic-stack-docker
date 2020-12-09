import requests
import urllib3
import json
import time
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

es_url = "https://192.168.1.14:9200"
es_username = 'elastic'
es_password = 'Admin123'
passwords = {}
passwords['elastic'] = 'Admin123'
passwords['apm_system'] = 'Admin123'
passwords['kibana'] = 'Admin123'
passwords['kibana_system'] = 'Admin123'
passwords['logstash_system'] = 'Admin123'
passwords['beats_system'] = 'Admin123'
passwords['remote_monitoring_user'] = 'Admin123'

# response = requests.get(url, auth = HTTPBasicAuth('elastic', 'Admin123'), verify='/home/thur/git/espy/ca.crt')

responCode = 404
max_retries = 3
while (responCode == 404) and max_retries > 0:
    endpoint = '/_security/user'
    url = '{}{}'.format(es_url, endpoint)
    print('Trying to authenticate: {} with user [{}]'.format(url, es_username))
    try:
        response = requests.get(url, auth = HTTPBasicAuth(es_username, es_password), verify=False)
        responCode = response.status_code

    except Exception as e:
        print('Exception: {}'.format(e))
        time.sleep(3)
        max_retries -= 1
        print('- - - - - - - - - - - - - - - -')
        print('Attempt to retry: {}'.format(max_retries))
        print('- - - - - - - - - - - - - - - -')
    else:
        if (responCode == 200):
            print('Authentication SUCCESS')
        elif (responCode == 401):
            print('Authentication Failure for user [{}]'.format(es_username))

if (responCode == 200):
    json_response = json.loads(response.content)
    print(json.dumps(json_response, indent=2))
    user_count = 0
    for username in json_response.keys():

        headers = {'Content-type': 'application/json'}
        endpoint = '/_security/user/{}/_password'.format(username)
        url = '{}{}'.format(es_url, endpoint)
        user_data = {}
        user_data['password'] = passwords[username]
        data_json = json.dumps(user_data)
        try:
            print('\nTrying user password change call {}'.format(url))
            response = requests.post(url, headers = headers, data = data_json, auth = HTTPBasicAuth(es_username, es_password), verify=False)
            responCode = response.status_code
            print('Response ({}):\n{}'.format(responCode, json.dumps(json.loads(response.content), indent=2)))
            if (responCode == 200):        
                print('Changed password for user [{}]'.format(username))
                if (username == es_username):
                    es_password = passwords[username]
        except Exception as e:
            print('Exception: {}'.format(e))
            
elif (responCode == 401):
    json_response = json.loads(response.content)
    print(json.dumps(json_response, indent=2))
    if 'error' in json_response.keys():
        print(json_response['error']['reason'])