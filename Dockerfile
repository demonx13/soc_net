FROM python:3.8.6
RUN pip install --upgrade pip

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

COPY ./req.txt .
RUN pip install -r req.txt

COPY . /usr/src/app/

RUN chmod 755 /usr/src/app/prestart.sh

#
#COPY ./entrypoint.sh .
#
#COPY . .

#ENTRYPOINT = ["/usr/src/app/entrypoint.sh"]
