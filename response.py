import requests
import json
from StringIO import StringIO
from datetime import datetime
from os import rename
import argparse

def backup(url, backup):
    url = url + '/scheduler/jobs'
    r = requests.get(url)
    date = datetime.utcnow()
    output_log_location = backup + str(date) + '.json' + '.new'
    with open(output_log_location,'w') as output:
        output.write(r.text)
    rename(output_log_location, backup + str(date) + '.json')

def restore(url, log_file_location):
    for line in open(log_file_location):
        io = StringIO(line)
        jsondecode = json.load(io)
        for item in jsondecode:
            if 'parents' in item:
                payload = json.dumps(item)
                urltosend = url + '/scheduler/dependency'
                headers = {'Content-type':'application/json'}
                r = requests.post(urltosend, data=payload, headers=headers)
                print (r.text)
            else:
                payload = json.dumps(item)
                urltosend = url + '/scheduler/iso8601'
                headers = {'Content-type': 'application/json'}
                r = requests.post(urltosend, data=payload, headers=headers)
                print (r.text)

def main():
    parser = argparse.ArgumentParser(description='Backups and restores Chronos jobs. By default, assumes you want to backup your jobs to chronosbackups/')
    parser.add_argument('-b', '--backup', help='Specifies whether to backup the Chronos jobs and where in the format chronosbackups/ and the folder must already exist.')
    parser.add_argument('-r', '--restore', help='Specifies whether to restore from a json file to the Chronos server.')
    parser.add_argument('-u', '--url', help='Specify URL for Chronos in the format http://chronos:4400', required=True)
    args = parser.parse_args()
    if args.backup != None:
        backup(args.url, args.backup)
    elif args.restore != None:
        restore(args.url, args.restore)

if __name__ == "__main__":
    main()
