from flask import Flask, render_template, request, redirect, url_for
from function import resize, save
import ctypes, subprocess

libc = ctypes.cdll.LoadLibrary("./c/sample.so")

app = Flask(__name__)

app.register_blueprint(resize.resize)
app.register_blueprint(save.save)

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
        
        inputfile = '/app/test_raw.txt'
        outputfile = '/app/test_enc.txt'
        
        libc.encrypt_image_file(inputfile.encode(), outputfile.encode())
        
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
    
@app.route('/compile')
def comp():
    return render_template('func.html')
    
@app.route('/action/compile')
def compile():
    subprocess.run(['gcc', './c/sample.c', '-shared', '-o', './c/sample.so'])
    return redirect('/compile')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")