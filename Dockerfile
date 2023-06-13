FROM python:3.11-slim-buster
RUN apt-get update && apt-get install -y gcc 
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt