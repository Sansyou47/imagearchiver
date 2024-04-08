FROM python:3.8
COPY /app /app
COPY requirements.txt /app
WORKDIR /app/c
RUN gcc -shared -O2 -o sample.so sample.c
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

#Pythonファイルの実行
CMD ["python", "-u", "app.py"]