FROM python:3.8-alpine
COPY ./requirements.txt /tmp/requirements.txt 
WORKDIR /app
RUN python3 -m pip install -r /tmp/requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
