FROM python:3.6
EXPOSE 5000
ADD . /app

WORKDIR /app

COPY requirements.txt /app
COPY templates /app

RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py
