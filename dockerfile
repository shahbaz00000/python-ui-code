FROM python:3.9-slim

WORKDIR /app

COPY main.py .

RUN pip install -r main.py

EXPOSE 5000

CMD ["python","main.py"]
