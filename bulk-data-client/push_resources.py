 #!/usr/bin/python

import json
import os
import requests

import sys, getopt
import os
import time


def transform_resource(resource):
    resource.pop('id')
    return json.dumps(resource)

def send_post(path, data, headers):
    response = requests.post(url = path, data = data, headers = headers)
    return response.status_code
                    

def push_data(input_dir, fhir_url="http://localhost:5555/fhir/"):
    
    print('\nDownloading data..\n')
    os.system("node . -d " + input_dir)
    print('\nStart pushing data..\n')
    
    headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

    for file_name in os.listdir(input_dir):
        try: 
            if not file_name.endswith('.ndjson'):
                continue;
            print(file_name)
            with open(input_dir + file_name, "r") as file:
                resources = file.read().splitlines()
                for r in resources:
                    resource = json.loads(r)
                    if 'resourceType' in resource.keys():
                        resource_type = resource.get('resourceType')
                        data = transform_resource(resource)
                        response_code = send_post(fhir_url + resource_type, data, headers)
                        if (response_code!=201):
                            print('Error: Unexpected response ', response)
                            continue; 
            os.remove(input_dir + file_name)
        except Exception as ex:
            print('An error has occurred: ', ex)




def main(argv):
   input_dir = ''
   url = os.getenv('SPARK_FHIR_URL', 'http://localhost:5555/fhir/')
   print('fhir_url=', url)
   push_data("/sample-apps-stu3/fhir-downloader/downloads/", url)

if __name__ == "__main__":
   main(sys.argv[1:])