FROM python:3.7
MAINTAINER Santu Chall <santuchal@gmail.com>

WORKDIR /app

EXPOSE 5000

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "src/main:app"]


ENTRYPOINT ["python", "src/main.py"]