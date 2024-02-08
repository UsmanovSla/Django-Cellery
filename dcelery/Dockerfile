FROM python:3.12.2-alpine3.19


WORKDIR /usr/src/app


# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# make sure all messages always reach console
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
