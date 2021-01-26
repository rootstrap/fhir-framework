Push Data
----------

- For each file in a certain directory, divides it into multiple resources.     
- Then, pushes each resource to the specified FHIR server.      
- After pushing resources in a file, removes the file from the directory   
- It keeps alive waiting for more files to be pushed   


## Environment variables    

The following environment variables are set:   
- FHIR_URL: url where spark Fhir server is listening    
- PYTHONUNBUFFERED: set to 1 if you want to see the output of the python script    
- DATA_PATH: url where data to be uploaded to the server is stored   
