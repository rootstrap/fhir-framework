Bulk Data Client
-----------------

This NodeJs client downloads bulk data in FHIR format for simulating patient's information  

Depends on [Bulk Data Client](https://github.com/smart-on-fhir/sample-apps-stu3/tree/master/fhir-downloader)    
The image can be found at [rootstrap/bulk-fhir-data-client](https://hub.docker.com/repository/docker/rootstrap/bulk-data-fhir-client)   
You can create your custom image by changing the Dockerfile and update the image's name at docker-compose.yml     


## Configuration
The configuration file [config.json](bulk-data-client/config.json). Contains the information to access the bulk data server.     
In case you need another configuration, you can re-build the image with the new config.json file.    

## RUN
You can run the container manually, executing: 
```console
docker run --name bulk-data-fhir-client rootstrap/bulk-data-fhir-client:latest 
```