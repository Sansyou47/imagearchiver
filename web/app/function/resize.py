from flask import Flask, render_template, request, Blueprint
from PIL import Image

resize = Blueprint("resize", __name__)

# オリジナル画像の保存先
imgLocation_origin = 'images/origin/'
# リサイズ画像の保存先
imgLocation_resized = 'images/downsize/'

def imgResize(weight):
    img = Image.open(imgLocation_origin + 'test.jpg')
    
    # 画像のサイズを取得
    before = img.size

    # 拡大・縮小の倍率を計算
    multiple = before[0] / weight

    # 元のアス比でリサイズ解像度を計算
    after = (weight, int(before[1] / multiple))
    
    # リサイズ処理
    img_resized = img.resize(after)
    
    meta = meta_generate(before, after)

    # リサイズ画像を保存（ファイル名にメタデータを付与）
    img_resized.save(imgLocation_resized + 'test' + '(' + str(meta) + ')' + '.jpg')

def meta_generate(src_before, src_after):
    if src_before[0] > src_after[0]:
        dmeta = 'downsizing,'
    else:
        dmeta = 'enlargement,'
    dmeta += 'resolution=' + str(src_after[0]) + 'x' + str(src_after[1])
    
    return dmeta