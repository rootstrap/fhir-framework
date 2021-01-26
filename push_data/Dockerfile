FROM python:3.9

RUN apt-get update && apt install -y python-pip  

RUN pip install requests

VOLUME /data

COPY push_resources.py /

CMD ["python", "/push_resources.py"]

