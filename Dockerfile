FROM docker.io/node:15-alpine as build

ENV NODE_ENV=production

WORKDIR /app/src/
ADD src/ /app/src/
RUN yarn install --frozen-lockfile
RUN yarn run generate

