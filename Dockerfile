FROM python:3.11-alpine

ENV FLASK_APP main.py
ENV FLASK_CONFIG prod

RUN adduser -D flaskuser
USER flaskuser

WORKDIR /home/flaskuser

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY main.py config.py boot.sh ./
RUN mkdir /home/flaskuser/data/

# runtime configuration
EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]
