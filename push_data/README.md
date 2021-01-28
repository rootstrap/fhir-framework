Push Data
----------

This is a python script that reads files in a directory and:   
- For each file divides it into multiple resources.     
- Then, pushes each resource to the specified FHIR server.      
- After pushing resources contained in a file, removes the file from the directory   
- It keeps alive waiting for more files to be pushed   

The image can be found at [rootstrap/push-fhir-data](https://hub.docker.com/repository/docker/rootstrap/push-fhir-data)

## Environment variables    

The following environment variables are set:   
- FHIR_URL: url where spark Fhir server is listening    
- PYTHONUNBUFFERED: set to 1 if you want to see the output of the python script    
- DATA_PATH: url where data to be uploaded to the server is stored   


## RUN
You can run the container manually, executing: 
```console
docker run --env FHIR_URL=http://spark:80/fhir/ DATA_PATH=/data/ -v {FILES_PATH}:/data --env --name push-fhir-data rootstrap/push-fhir-data:latest 
```
Replace {FILES_PATH} with the path for the files that you would like to push to the server. 

