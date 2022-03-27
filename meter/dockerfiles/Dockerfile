FROM python:3

WORKDIR /usr/src/app

COPY ./meter/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./meter/src .
COPY ./shared ./shared

CMD [ "python", "./main.py" ]