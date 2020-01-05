FROM alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY . /data/web/

# Setup
# ENV http_proxy=http://pfrie-std.proxy.e2.rie.gouv.fr:8080
# ENV https_proxy=http://pfrie-std.proxy.e2.rie.gouv.fr:8080
RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

# Clean
RUN apk del -r python3-dev postgresql

# Prepare
RUN mkdir -p /staticfiles_ff
