FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
        && apt-get install -y --no-install-recommends \
            postgresql-client \
        && rm -rf /var/lib/apt/lists/*