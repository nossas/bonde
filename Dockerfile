FROM node:7-alpine
MAINTAINER Nossas <tech@nossas.org>

RUN apk add --no-cache make gcc g++ python git
RUN mkdir /code
VOLUME /code
WORKDIR /code
COPY . /code
RUN npm install && npm run build
EXPOSE 5000
CMD ["node", "./bin/server"]
