FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install Flask
EXPOSE 5000
CMD ["python", "application.py"]