FROM python:3.9-buster

WORKDIR /app
# Double Check comments / fileset2 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
