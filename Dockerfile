FROM python:3.9.11

WORKDIR /var/www

COPY /Parallel/requirements.txt .

RUN pip install -r requirements.txt

COPY Parallel_project .

CMD ["fastapi" , "run" , "main.py"]