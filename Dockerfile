FROM python:2.7-alpine

ENV APP_HASH=requiredForBuildAndWillBeAutoUpdatedAfterBuild
ENV SALT=requiredForBuildAndWillBeAutoUpdatedAfterBuild
ENV SECRET_KEY=requiredForBuildAndWillBeAutoUpdatedAfterBuild
ENV DEFAULT_SALT=requiredForBuildAndWillBeAutoUpdatedAfterBuild

# bash, curl, openssh, iproute2 required for heroku container ssh
RUN apk add --update \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    postgresql-dev \
    build-base \
    linux-headers \
    libffi-dev \
    bash \
    curl \
    openssh \
    iproute2 \
    && rm -rf /var/cache/apk/* \

# required for heroku container ssh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN mkdir -p /app/.profile.d
COPY server_files/heroku_ssh/heroku-exec.sh /app/.profile.d/

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
COPY requirements /code/requirements
# required for Twisted package which installs broken incremental .egg file
# must be installed independly
RUN pip install incremental==16.10.1
RUN pip install -r requirements.txt

COPY . /code/
COPY server_files/daphne.supervisor.conf /etc/supervisor/conf.d/
COPY server_files/supervisord.conf /etc/supervisor/
RUN mkdir /run/daphne
RUN mkdir /var/log/supervisor/
RUN touch /var/log/supervisor/supervisord.log

RUN #python manage.py collectstatic --noinput

CMD supervisord -n -c /etc/supervisor/supervisord.conf
