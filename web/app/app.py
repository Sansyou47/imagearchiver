from flask import Flask, render_template, request, redirect, url_for
from function import resize, save, func
from ctypes import *
import ctypes, subprocess

libc = ctypes.cdll.LoadLibrary('/app/c/sample.so')
# 関数の引数の型を設定
libc.encrypt_image_file.argtypes = [c_char_p, c_char_p]

app = Flask(__name__)

app.register_blueprint(save.save)
app.register_blueprint(func.func)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form.get('preset')
        quality = request.form.get('quality')
        image = request.files.get('example')
        
        if num is None:
            return redirect('/')
        if quality is None:
            quality = 75
        quality = int(quality)
        
        if image is None:
            return redirect('/')
        
        if save.extensionJudge(image.filename) == False:
            return redirect('/')
        
        imageName = save.imgSave(image)
        
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
        
        libc.encrypt_image_file(imageName.encode(), imageName.encode())
        return redirect('/')
    else:
        return render_template('index.html')
    
@app.route('/fib', methods = ['GET', 'POST'])
def fib():
    if request.method == 'POST':
        num = request.form.get('number')
        preset = request.form.get('preset')
        if num is None:
            return redirect('/fib')
        num = int(num)
        if preset == 1:
            result = fib(num)
        else:
            result = libc.fib(num)
        return str(result)
    else:
        return render_template('fib.html')
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")