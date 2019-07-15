FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat


WORKDIR /usr/src/app/

COPY /server/Pipfile .
COPY /server/Pipfile.lock .

RUN pip install pipenv

RUN pipenv install

COPY /server/ .

EXPOSE 8000

# copy entrypoint.sh
COPY scripts/entrypoint.sh /usr/src/app/scripts/entrypoint.sh

RUN ["chmod", "+x", "/usr/src/app/scripts/entrypoint.sh"]

ENTRYPOINT ["/usr/src/app/scripts/entrypoint.sh"]

CMD ["pipenv", "run", "server"]