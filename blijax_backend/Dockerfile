FROM python:3.11
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver"]
EXPOSE 8000