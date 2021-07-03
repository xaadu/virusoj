FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10
ENV PYTHONUNBUFFERED 1

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Dhaka /etc/localtime
RUN echo "Asia/Dhaka" > /etc/timezone
RUN apk del tzdata

#RUN apk add --update musl-dev gcc libffi-dev
RUN apk add --update --no-cache --virtual .build-deps musl-dev gcc libffi-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apk del .build-deps

WORKDIR /usr/src/app
COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7003", "--proxy-headers"]
