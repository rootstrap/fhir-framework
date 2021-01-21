# fhir-framework

Fhir server to download generated patient's data. It consist of the following components:

1. [Fhir Server](https://github.com/FirelyTeam/spark/)
The Fhir Server implements FHIR specification, exposes a REST API to access FHIR data. 

2. MongoDB 
This database is used by the Fhir Server to store the information. 

3. [Bulk Data Server](https://github.com/smart-on-fhir/bulk-data-server.git)
Exposes an API to generate Fhir resources.

4. Bulk Data Client
Consumes the API of the bulk data server and saves it locally. [Here](https://github.com/smart-on-fhir/sample-apps-stu3/tree/master/fhir-downloader) is the implementation of the client. 
A python script is executed to push these resources to the Fhir Server. 

## Execution 

```bash 
	docker-compose up
```

You can access to the server at [http://localhost:5555/](http://localhost:5555/). 

## Configuration / Environment variables 

### Fhir Server 
It is necessary to specify the following environment variables:
- StoreSettings__ConnectionString: mongodb url
- SparkSettings__Endpoint: url that the server will be listening 

### MongoDB
User and password  

### Bulk Data Server
It is necessary to SPARK_FHIR_URL to set the url for spark server.  

### Bulk Data Client
1. The configuration file [config.json](bulk-data-client/config.json). Contains the information to access the bulk data server. 
In case you need another configuration, you can re-build the image with the new config.json file. 

2. Set the environment variable BASE_URL with the url that the bulk data server is listening 
