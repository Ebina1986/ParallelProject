FROM python:3.9.11

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["fastapi" , "run" , "main.py"]
