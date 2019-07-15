FROM node:10.16.0-slim

WORKDIR /usr/src/app/

COPY /client/package-lock.json .
COPY /client/package.json .

RUN npm install

COPY /client/ .

EXPOSE 8080

CMD ["npm", "run", "serve"]