FROM python:3.11-slim

WORKDIR usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "dev", "python", "main.py"]