from flask import Flask, render_template, request, Blueprint
from PIL import Image
import math

resize = Blueprint("resize", __name__)

def resize_image(res):
    img = Image.open("images/origin/test2.jpg")
    image_x = img.width
    image_y = img.height

    multiple = int(image_x / res)

    size = (res, int(image_y / multiple))

    img_resized = img.resize(size)

    img_resized.save("images/downsize/test_resized.jpg")


@resize.route('/func', methods=["POST"])
def func():
    if request.method == "POST":
        num = request.form.get("submit")
        if num == "1":
            resize_image(155)
        elif num == "2":
            resize_image(300)
        elif num == "3":
            resize_image(100)
        return render_template('index.html')
