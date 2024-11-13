# Dockerfile
FROM python:3.9

RUN pip install psutil

COPY app/monitor.py /app/monitor.py

WORKDIR /app

CMD ["python", "monitor.py"]
