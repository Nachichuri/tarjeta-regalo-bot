FROM python

WORKDIR /bot
COPY . .

RUN apt-get update && apt-get install -y firefox-esr cargo
RUN pip install selenium webdriver-manager python-telegram-bot

CMD ["python", "main.py"]
