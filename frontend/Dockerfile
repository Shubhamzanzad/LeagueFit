FROM python:3.9-slim AS build
WORKDIR /app
COPY frontend.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "frontend.py"]
