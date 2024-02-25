from flask import Flask, render_template, request, Blueprint
from PIL import Image
import math

resize = Blueprint("resize", __name__)

imgLocation_origin = 'images/origin/'
imgLocation_resized = 'images/downsize/'

def imgResize(res):
    img = Image.open(imgLocation_origin + 'test.jpg')
    image_x = img.width
    image_y = img.height

    multiple = int(image_x / res)

    size = (res, int(image_y / multiple))
    
    meta = 'resize=' + str(size)

    img_resized = img.resize(size)

    img_resized.save(imgLocation_resized + 'test' + '_resized' + '(' + str(meta) + ')' + '.jpg')


@resize.route('/func', methods=["POST"])
def func():
    if request.method == "POST":
        num = request.form.get("submit")
        if num == "1":
            imgResize(155)
        elif num == "2":
            imgResize(300)
        elif num == "3":
            imgResize(600)
        return render_template('index.html')
