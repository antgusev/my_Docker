FROM python:3.12
WORKDIR /src
ENV MY_ENV=antgusev_31_10_24
COPY . .
RUN pip3 install --no-cache-dir --upgrade -r smart_home/requirements.txt
RUN apt-get update && apt-get install sqlite3
RUN sqlite3 netology_smart_home.db
RUN python smart_home/manage.py makemigrations && python smart_home/manage.py migrate
CMD ["python3", "-u", "smart_home/manage.py", "runserver", "--host", "0.0.0.0", "--port", "8000"]
