# fhir-framework

Fhir server to download generated patient's data. It consist of the following components:

1. [Fhir Server](https://github.com/FirelyTeam/spark/)
The Fhir Server implements FHIR specification, exposes a REST API to access FHIR data. 

2. [Bulk Data Server](https://github.com/smart-on-fhir/bulk-data-server.git)
Exposes an API to generate Fhir resources.

3. Bulk Data Client
Consumes the API of the bulk data server and saves it locally. [Here](https://github.com/smart-on-fhir/sample-apps-stu3/tree/master/fhir-downloader) is the implementation of the client. 
A python script is executed to push these resources to the Fhir Server. 

## Execution 

```bash 
	docker-compose up
```

You can access to the server at [http://localhost:5555/](http://localhost:5555/). 

