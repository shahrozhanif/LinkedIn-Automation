FROM python:3.11.6-alpine
WORKDIR /app
COPY . /app/
RUN python -m pip install --upgrade pip==24.2
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]