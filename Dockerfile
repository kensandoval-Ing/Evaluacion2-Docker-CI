FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --disable-pip-version-check --progress-bar off -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
