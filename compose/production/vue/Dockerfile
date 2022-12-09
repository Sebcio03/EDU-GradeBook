FROM node:16-alpine as builder

WORKDIR /app

COPY ./frontend/package-lock.json ./
COPY ./frontend/package.json ./

RUN npm i -f
COPY ./frontend .
RUN npm run build

FROM nginx:1.19.2-alpine
COPY --from=builder ./app/dist /usr/share/nginx/html

COPY ./frontend/nginx/nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]