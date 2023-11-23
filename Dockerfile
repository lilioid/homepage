FROM docker.io/node:20-alpine as build
RUN npm install -g pnpm

WORKDIR /usr/local/src/homepage/src/
ADD src/package.json src/pnpm-lock.yaml src/.npmrc /usr/local/src/homepage/src/
RUN pnpm install --frozen-lockfile
ADD src/ /usr/local/src/homepage/src/
RUN pnpm run build

# build final image with static content
FROM docker.io/node:20-alpine as final
WORKDIR /usr/local/src/homepage

RUN apk add --no-cache nginx supervisor
ADD docker/nginx.conf /etc/nginx/http.d/default.conf
ADD docker/supervisord.conf /etc/supervisord.conf
CMD ["supervisord", "--configuration=/etc/supervisord.conf"]

COPY --from=build /usr/local/src/homepage/src/.output/ /usr/local/src/homepage/
EXPOSE 80/tcp
