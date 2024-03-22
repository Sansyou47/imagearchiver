FROM python:3.8
WORKDIR /app
COPY /app .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# WORKDIR /app/c
# RUN gcc -shared -O2 -o sample.so sample.c
# WORKDIR /app

#Pythonファイルの実行
# CMD ["python", "-u", "app.py"]

CMD uwsgi --http=0.0.0.0:8000 --wsgi-file=/app/app.py --callable=app