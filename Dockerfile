FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN apt-get update && apt-get install -y \
    libgomp1 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

    
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Lance le serveur Django sur le port 8000
CMD ["python", "webapp/manage.py", "runserver", "0.0.0.0:8000"]