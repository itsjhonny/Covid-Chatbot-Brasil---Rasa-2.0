FROM ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa
ADD . /app/

RUN pip3 install -U spacy

RUN python3 -m spacy download en_core_web_md && \
    python3 -m spacy link en_core_web_md pt

RUN pip3 install recognizers-text-suite

# RUN cd /app && rasa train

RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh
