FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir
COPY . ./
CMD ["gunicorn", "core.wsgi:application", "--bind", "0:8000" ]
