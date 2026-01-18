FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir /data

COPY . .

EXPOSE 5000

ENV DEBUG=False
ENV PORT=5000
ENV DATABASE=/data/database.txt

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]