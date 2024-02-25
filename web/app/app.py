from flask import Flask, render_template, request, redirect, url_for
from function import resize

app = Flask(__name__)

app.register_blueprint(resize.resize)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form.get("submit")
        quality = request.form.get("radio")
        if quality is None:
            quality = 75
        quality = int(quality)
        if num == "1":
            resize.imgResize(155, quality)
        elif num == "2":
            resize.imgResize(300, quality)
        elif num == "3":
            resize.imgResize(600, quality)
        else:
            res = request.form.get("text")
            if res == '':
                return redirect('/')
            else:
                resize.imgResize(int(res), quality)
        return redirect('/')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")