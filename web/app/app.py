from flask import Flask, render_template, request, redirect, url_for
from function import resize

app = Flask(__name__)

app.register_blueprint(resize.resize)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")