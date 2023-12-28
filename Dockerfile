FROM docker.io/node:20-alpine as build
RUN npm install -g pnpm

WORKDIR /usr/local/src/homepage
ADD . /usr/local/src/homepage
RUN pnpm install --frozen-lockfile
RUN pnpm run build



FROM docker.io/nginx:mainline as final
ADD docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /usr/local/src/homepage/dist /usr/share/nginx/html
