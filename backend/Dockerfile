FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir scikit-learn
RUN pip install --no-cache-dir streamlit
RUN pip install --no-cache-dir typing
RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir uvicorn
EXPOSE 8000
CMD ["python", "backend.py"]
