FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV REDIS_HOST=redis-server
CMD ["python", "application.py"]