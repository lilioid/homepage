FROM docker.io/node:20 as build
RUN npm install -g pnpm

WORKDIR /usr/local/src/homepage/src/
ADD src/package.json src/pnpm-lock.yaml src/.npmrc /usr/local/src/homepage/src/
RUN pnpm install --frozen-lockfile
ADD src/ /usr/local/src/homepage/src/
RUN pnpm run build

# build final image with static content
FROM docker.io/node:20 as final
WORKDIR /usr/local/src/homepage
COPY --from=build /usr/local/src/homepage/src/.output/ /usr/local/src/homepage/
CMD ["node", "/usr/local/src/homepage/server/index.mjs"]
ENV PORT=80
EXPOSE 80/tcp
