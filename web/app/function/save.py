from flask import Flask, render_template, request, Blueprint
from flaskext.mysql import MySQL
from PIL import Image
from function import variable
import os

save = Blueprint("save", __name__)

mysql = None

# 画像保存関数
def imgSave(img, mysql):
    imageName = img.filename
    ext = extensionJudge(imageName)
    if ext == False:
        return False
    else:
        img.save(variable.imgLocation_origin + imageName)
        file_size = os.path.getsize(variable.imgLocation_origin + imageName)
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO images(imageName, filePath, fileType, fileSize,userId) VALUES (%s, %s, %s, %s, %s)', (imageName, variable.imgLocation_origin, ext, file_size, 1))
        cursor.connection.commit()
        cursor.close()
        return imageName

# 対応した拡張子か判定する関数（対応していれば拡張子を返す）
def extensionJudge(imgName):
    ext = imgName.split('.')[-1]
    if ext not in variable.supportedExtentionList:
        return False
    else:
        if ext == 'jpeg':
            ext = 'jpg'
        return ext