FROM python:3.8
WORKDIR /app
COPY /app .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /c
RUN gcc -shared -O2 -o sample.so sample.c

#Pythonファイルの実行
CMD ["python", "-u", "app.py"]