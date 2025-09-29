FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}
RUN sed -i "s|__SERVER_NAME__|${SERVER_NAME}|g" /static/chat.html

EXPOSE 8000

CMD ["uvicorn", "logic.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
