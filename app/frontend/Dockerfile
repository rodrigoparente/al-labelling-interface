# Stage 1: Build app

FROM node:16-alpine AS builder

RUN mkdir /app
WORKDIR /app

COPY . .

RUN npm ci && \
    npm run build


# Stage 2: Deploy app

FROM nginx:1.22

RUN rm -rf /usr/share/nginx/html/*

COPY nginx/default.conf /etc/nginx/conf.d/

COPY --from=builder /app/dist/ /usr/share/nginx/html/
