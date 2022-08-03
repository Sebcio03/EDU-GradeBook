FROM node:16-alpine

WORKDIR /app

COPY ./frontend/package-lock.json ./
COPY ./frontend/package.json ./

RUN npm i

COPY ./frontend .

ENTRYPOINT [ "npm","run", "dev", "--host"] 