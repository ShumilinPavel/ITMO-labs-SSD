FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
