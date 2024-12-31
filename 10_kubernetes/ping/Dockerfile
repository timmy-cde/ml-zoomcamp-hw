FROM python:3.11.10-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ping.py ./

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "ping:app" ]

# to build: docker build -t ping:v001 .
# to run: docker run -it -p 9696:9696 --rm ping:v001 
