FROM python:3.12-slim

WORKDIR /app

# Copy semua file project
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "flask_app/app.py"]
