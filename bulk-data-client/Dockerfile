FROM node:12.18.0

RUN apt-get update && apt install -y \
	python-pip \
	git 

RUN pip install requests

RUN git clone https://github.com/smart-on-fhir/sample-apps-stu3.git

COPY config.json sample-apps-stu3/fhir-downloader/

WORKDIR sample-apps-stu3/fhir-downloader

RUN npm install

CMD ["node", ".", "-d", "downloads"]