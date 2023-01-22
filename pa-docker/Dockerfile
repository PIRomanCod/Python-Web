FROM python:3.10

WORKDIR /pa-docker
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "pa"]