FROM python:3.7
WORKDIR /app
EXPOSE 5000

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "src/main.py"]