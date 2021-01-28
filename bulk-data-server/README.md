Bulk Data Server
-----------------

This server exposes an API to generate bulk Fhir data. 

Depends on [Bulk Data Server](https://github.com/smart-on-fhir/bulk-data-server.git)   
The image can be found at [rootstrap/bulk-fhir-data-server](https://hub.docker.com/repository/docker/rootstrap/bulk-data-fhir-server)  

## Environment variables    
It is necessary to BASE_URL to set the url to expose.     


## RUN 
You can run the container manually, executing: 
```console
docker run -d  --env BASE_URL=BASE_URL=http://bulk-data-fhir-server:9443  -p  9443:9443 --name bulk-data-fhir-server rootstrap/bulk-data-fhir-server:latest 
```

You can access to the server at [http://localhost:9443/](http://localhost:9443/)

## Generate config.json 
1. Go to [http://localhost:9443/](http://localhost:9443/)
2. Press 'Generate' button to generate JWKS keys 
3. Choose the configuration that you want 
4. Press 'Download as JSON' button 

This configuration can be used in a client that invokes this server to generate information.
The configuration contains the Keys to Authenticate with the server as well as information about the data that you want to download. 

The client provided already has a config.json by default, if you would like to change this configuration you should build the docker image with it. 

