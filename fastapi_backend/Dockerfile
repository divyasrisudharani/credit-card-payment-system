FROM python:3.12-slim

WORKDIR /app

COPY fastapi_backend/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY fastapi_backend ./fastapi_backend
COPY django_backend ./django_backend

WORKDIR /app/fastapi_backend

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]