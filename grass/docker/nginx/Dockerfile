FROM nginx:latest

RUN rm /etc/nginx/cond.d/default.conf
COPY nginx.conf /etc/nginx/cond.d
COPY proxy_params /etc/nginx