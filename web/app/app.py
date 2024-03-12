from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from function import resize, save, variable
import ctypes, subprocess, os, time

libc = ctypes.cdll.LoadLibrary("./c/sample.so")

app = Flask(__name__)

app.config["MYSQL_DATABASE_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DATABASE_DB"] = os.getenv("MYSQL_DATABASE")
app.config["MYSQL_DATABASE_HOST"] = "mysql"

mysql = MySQL(app)

app.register_blueprint(resize.resize)
app.register_blueprint(save.save)

resize.mysql = mysql
save.mysql = mysql

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form.get('preset')
        quality = request.form.get('quality')
        image = request.files.get('example')
        do_encrypt = request.form.get('do_encrypt')
        do_encrypt = int(do_encrypt)
        
        if num is None:
            return redirect('/')
        if quality is None:
            quality = 75
        quality = int(quality)
        
        if image is None:
            return redirect('/')
        
        # 画像の保存と同時に拡張子を検査し、非対応の拡張子だった場合はfalseを返してリダイレクト
        imageName = save.imgSave(image, mysql)
        if imageName == False:
            return redirect('/')
        
        if num == "1":
            resize.imgResize(imageName, 155, quality)
        elif num == "2":
            resize.imgResize(imageName, 300, quality)
        elif num == "3":
            resize.imgResize(imageName, 600, quality)
        else:
            res = request.form.get("text")
            if res == '':
                return redirect('/')
            else:
                res = int(res)
                resize.imgResize(imageName, res, quality)
        if do_encrypt == 1:
            # 暗号化するファイルのパス
            inputfile = '/app/images/origin/' + imageName
            # 暗号化後のファイルのパス
            outputfile = '/app/' + variable.imgLocation_encrypted + imageName
            variable.enc_file(inputfile.encode(), outputfile.encode())
        elif do_encrypt == 2:
            # 暗号化するファイルのパス
            inputfile = '/app/images/origin/' + imageName
            # 暗号化後のファイルのパス
            outputfile = '/app/' + variable.imgLocation_encrypted + imageName
            libc.encrypt_image_file(inputfile.encode(), outputfile.encode())
        
        return redirect('/')
    else:
        return render_template('index.html')
    
@app.route('/fib', methods = ['GET', 'POST'])
def fib():
    if request.method == 'POST':
        num = request.form.get('number')
        count = request.form.get('count')
        preset = request.form.get('preset')
        if num is None:
            return redirect('/fib')
        num = int(num)
        count = int(count)
        total_time = 0
        preset = int(preset)
        if preset == 1:
            for i in range(count):
                start_time = time.time()
                result = fibn(num)
                end_time = time.time()
                pre = 'Python'
                total_time += end_time - start_time
        else:
            for i in range(count):
                start_time = time.time()
                result = libc.fib(num)
                end_time = time.time()
                pre = 'C'
                total_time += end_time - start_time
            
        average_time = total_time / count * 1000  # ミリ秒単位に変換
        return '計算結果：' + str(result) + ', ' + '実行回数：' + str(count) + ', 平均時間：' + format(average_time, '.4f') + 'ミリ秒, ' + '言語：' + pre  # 4桁まで表示
    else:
        return render_template('fib.html')
    
@app.route('/compile')
def comp():
    return render_template('func.html')
    
@app.route('/action/compile')
def compile():
    subprocess.run(['gcc', './c/sample.c', '-shared', '-o', './c/sample.so'])
    return redirect('/compile')

def fibn(n):
    if n <= 1:
        return n
    return fibn(n - 1) + fibn(n - 2)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")