FROM rasa/rasa:latest-full

WORKDIR /app
COPY . /app
COPY ./data /app/data
COPY ./actions /app/actions

# Change back to root user to install dependencies
USER root
RUN pip install --upgrade pip

RUN python -m spacy download en_core_web_md && \
    python -m spacy link en_core_web_md pt

# Switch back to non-root to run code
USER 1001

RUN  rasa train 


VOLUME /app
VOLUME /app/data
VOLUME /app/models
VOLUME /app/actions


CMD [ "run","-m","/app/models","--enable-api","--cors","*","--debug" ]