import requests
import json
from StringIO import StringIO

def main():
    url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/jobs'
    r = requests.get(url)
    io = StringIO(r.text)
    jsondecode = json.load(io)
    print jsondecode
    url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/job/' + 'abc_1_1'
    r = requests.delete(url)
    url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/job/' + 'abc_2'
    r = requests.delete(url)
    url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/job/' + 'abc_1'
    r = requests.delete(url)
    url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/job/' + 'abc'
    r = requests.delete(url)
    for item in jsondecode:
        if "parents" in item:
            payload = {"async":item["async"], "command":item["command"], "epsilon":item["epsilon"], "errorCount":item["errorCount"], "lastError":item["lastError"], "lastSuccess":item["lastSuccess"], "name":item["name"], "owner":item["owner"], "parents":item["parents"], "retries":item["retries"], "successCount":item["successCount"]}
            url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/dependency'
            headers = {'Content-type':'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print r.text
        else:
            payload = {"schedule":item["schedule"], "name":item["name"], "epsilon":item["epsilon"], "command":item["command"], "owner":item["owner"], "async":item["async"]}
            url = 'http://nyvimeochrono1.vimeows.com:4400/scheduler/iso8601'
            headers = {'Content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print r.text
main()
