FROM python:3

WORKDIR /twitterBot

COPY * ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./bot/py/__main__.py" ]
