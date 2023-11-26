FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY /etc/letsencrypt/live/grass-job.ru-0001/ /etc/letsencrypt/live/grass-job.ru/
# COPY /etc/letsencrypt/ssl-dhparams.pem /etc/letsencrypt/ssl-dhparams.pem
# COPY /etc/letsencrypt/options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf