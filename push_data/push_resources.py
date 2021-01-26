 #!/usr/bin/python

import json
import os
import requests

import sys, getopt
import os
import time
import shutil


def transform_resource(resource):
    resource.pop('id')
    return json.dumps(resource)

def send_post(path, data, headers):
    response = requests.post(url = path, data = data, headers = headers)
    if (response.status_code!=201):
        print('Error: Unexpected response ', response)
        return False
    return True


def process_file(file_name, input_dir, fhir_url):
    if file_name =='':
        return;
    if os.path.isdir(inputdir + file_name):
        shutil.rmtree(inputdir + file_name)
        return;
    if not file_name.endswith('.ndjson'):
        return;
    print('Processing file ', file_name)
    with open(input_dir + file_name, "r") as file:
        resources = file.read().splitlines()
        headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
        for r in resources:
            resource = json.loads(r)
            if 'resourceType' in resource.keys():
                resource_type = resource.get('resourceType')
                data = transform_resource(resource)
                result = send_post(fhir_url + resource_type, data, headers)
                if (not result):
                    return;
    os.remove(input_dir + file_name)


def push_data(input_dir, fhir_url="http://localhost:5555/fhir/"):
    while(True):
        for file_name in os.listdir(input_dir):
            try: 
                process_file(file_name, input_dir, fhir_url)
            except Exception as ex:
                print('An error has occurred: ', ex)
        print('Waiting for files')
        time.sleep(60)


if __name__ == "__main__":
    inputdir = os.getenv('DATA_PATH', '/data/') 
    url = os.getenv('FHIR_URL', 'http://localhost:5555/fhir/')
    push_data(inputdir, url)