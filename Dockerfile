FROM python:3.12-alpine

WORKDIR /app
RUN apk update && apk upgrade
RUN apk update && apk upgrade --no-cache
RUN apk upgrade --no-cache libcrypto3 libssl3
# Double Check comments / Fixed for Demo
RUN pip3 install --upgrade pip setuptools

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
