FROM rasa/rasa-sdk:2.2.0

WORKDIR /app

USER root

COPY ./actions /app/actions

USER 1001