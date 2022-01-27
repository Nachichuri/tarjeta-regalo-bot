FROM python

WORKDIR /bot
COPY . .

RUN tar -xvzf dependencies.tar.gz
RUN apt-get update && \
    apt-get install ./dependencies/* -y && \
    apt-get install cargo -y
RUN pip install selenium python-telegram-bot

CMD ["python", "main.py"]
