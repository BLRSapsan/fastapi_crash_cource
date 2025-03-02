FROM python:3.13-slim

COPY . .

RUN pip insall -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
