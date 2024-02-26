from flask import Flask, render_template, request, Blueprint
from PIL import Image
from function import variable

save = Blueprint("save", __name__)

# 画像保存関数
def imgSave(img):
    imageName = img.filename
    img.save(variable.imgLocation_origin + imageName)
    return imageName

# 対応した拡張子か判定する関数
def extensionJudge(imgName):
    if imgName.split('.')[-1] not in variable.supportedExtentionList:
        return False
    else:
        return True