FROM python:3.10-buster@sha256:31a8498af27dba1f431f2df60189ca79ff5f440cfa7b6dea2da6ab15c74abcd4

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD ["uvicorn", "fastapiredis.application:app", "--host", "0.0.0.0"]
