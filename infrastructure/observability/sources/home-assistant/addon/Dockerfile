ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN \
    apk add --no-cache python3 tzdata \
    && mkdir -p /etc/services.d/midnightlabs-ha-observability

COPY app.py /app.py
COPY run.sh /etc/services.d/midnightlabs-ha-observability/run

RUN \
    chmod 0755 \
        /app.py \
        /etc/services.d/midnightlabs-ha-observability/run
