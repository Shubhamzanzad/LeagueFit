FROM python:3.9-slim AS build
WORKDIR /app
COPY frontend.py .
COPY requirements.txt .
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir scikit-learn
RUN pip install --no-cache-dir streamlit
RUN pip install --no-cache-dir typing
RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir uvicorn
EXPOSE 8501
CMD ["streamlit", "run", "frontend.py"]
