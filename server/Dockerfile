FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10
ENV PYTHONUNBUFFERED 1

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Dhaka /etc/localtime
RUN echo "Asia/Dhaka" > /etc/timezone
RUN apk del tzdata

COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app
COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7003", "--proxy-headers"]
