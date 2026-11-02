FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

# base command
ENTRYPOINT ["python", "commerce_utils.py"]

# default argument values
CMD ["50", "13"]
