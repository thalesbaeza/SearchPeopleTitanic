FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir psycopg2-binary

CMD ["python"]