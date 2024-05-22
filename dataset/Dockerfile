FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# RUN mkdir /app/logs
EXPOSE 8008
CMD ["python", "server.py"]
