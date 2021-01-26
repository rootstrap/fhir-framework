Bulk Data Client
-----------------

Depends on [Bulk Data Client](https://github.com/smart-on-fhir/sample-apps-stu3/tree/master/fhir-downloader)    

- Downloads bulk data in fhir format for simulating patient's information  
- Runs on nodejs, a Dockerfile is provided.    
- The image can be found at [rootstrap/bulk-fhir-data-client](https://hub.docker.com/repository/docker/rootstrap/bulk-data-fhir-client)   
- You can create your custom image by changing the Dockerfile and update image's name at docker-compose.yml     


## Configuration
The configuration file [config.json](bulk-data-client/config.json). Contains the information to access the bulk data server.     
In case you need another configuration, you can re-build the image with the new config.json file.    

## Environment variables  
Set the environment variable BASE_URL with the url that the bulk data server is listening     
