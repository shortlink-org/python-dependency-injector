FROM python:3.10-buster@sha256:31a8498af27dba1f431f2df60189ca79ff5f440cfa7b6dea2da6ab15c74abcd4

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

CMD uvicorn webapp.application:app --host ${HOST} --port ${PORT}
