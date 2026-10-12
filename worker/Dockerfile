FROM mcr.microsoft.com/devcontainers/universal:6.1.10-noble

USER root

COPY factory_prepare.py /usr/local/bin/factory-prepare

RUN chmod +x /usr/local/bin/factory-prepare \
    && bash -c '\
        set -e; \
        command -v bash; \
        command -v git; \
        command -v python3; \
        command -v php; \
        command -v composer; \
        command -v node; \
        command -v npm \
    '

ENV COMPOSER_ALLOW_SUPERUSER=1