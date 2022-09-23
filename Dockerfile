FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r ./requirements.txt

CMD uvicorn --host=0.0.0.0 --port 8000 assignment.main:app --reload