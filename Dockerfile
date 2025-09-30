FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ARG SERVER_NAME
RUN sed -i "s|http://localhost:8000|${SERVER_NAME}|g" /app/static/chat.html

EXPOSE 8000

CMD ["uvicorn", "logic.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
