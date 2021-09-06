FROM python:3.8.0-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY /app .
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]