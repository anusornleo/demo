# Stage 1: Build
FROM node:20-bullseye as builder

WORKDIR /app
COPY . .
RUN rm -rf node_modules yarn.lock
RUN yarn
RUN yarn install --immutable
RUN yarn build

# Stage 2: Run
FROM node:20-bullseye

WORKDIR /app
COPY --from=builder /app/.output ./.output
COPY --from=builder /app/package.json ./
# ติดตั้ง production-only dependencies
RUN yarn install --production --ignore-scripts

CMD ["node", ".output/server/index.mjs"]
