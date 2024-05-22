FROM python:3.9-slim
WORKDIR /app/
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# RUN mkdir /app/logs
EXPOSE 8000
CMD [ "python", "backend.py" ]
