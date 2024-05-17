FROM python:3.10-alpine

WORKDIR /app/

COPY ./requirements.txt .
RUN apk update && apk add --no-cache gcc && pip install -r requirements.txt
COPY . .
# RUN pip install --no-cache-dir pandas
# RUN pip install --no-cache-dir scikit-learn
# RUN pip install --no-cache-dir streamlit
# RUN pip install --no-cache-dir typing
# RUN pip install --no-cache-dir fastapi
# RUN pip install --no-cache-dir uvicorn

# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "backend.py"]
