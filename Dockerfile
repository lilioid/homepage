FROM docker.io/node:16-alpine as build

WORKDIR /app/src/
ADD src/package.json src/yarn.lock /app/src/
RUN yarn install --frozen-lockfile
ADD src/ /app/src/
RUN rm -rf /app/src/build /app/src/.svelte-kit
RUN yarn run build
RUN find build -name '*.html' -exec sed -i -E 's|new URL\("http://prerender/(.*?)"\)|new URL(`${window.location.href}`)|' {} +

# build final image with static content
FROM docker.io/nginx:1.19-alpine as final
ADD docker/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80/tcp
COPY --from=build /app/src/build /var/www
