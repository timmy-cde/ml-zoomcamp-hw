FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "gateway:app" ]


# docker build -t zoomcamp-10-gateway:002 -f image-gateway.dockerfile .

# docker run -it --rm \
#     -p 9696:9696 \
#     zoomcamp-10-gateway:001