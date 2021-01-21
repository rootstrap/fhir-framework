FROM node:12.18.0

RUN apt-get update && apt-get install -y git 

RUN git clone https://github.com/smart-on-fhir/bulk-data-server.git
   
WORKDIR bulk-data-server

RUN npm install

EXPOSE 9443

CMD ["npm", "start"]