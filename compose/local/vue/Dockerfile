FROM node:16-alpine

WORKDIR /app

COPY ./frontend/package-lock.json ./
COPY ./frontend/package.json ./

RUN ["npm", "install"]

COPY ./frontend .

ENTRYPOINT ["npm", "run", "dev"]