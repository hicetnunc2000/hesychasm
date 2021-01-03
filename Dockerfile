FROM python:latest

RUN pip install --upgrade pip

RUN apt-get update 

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]