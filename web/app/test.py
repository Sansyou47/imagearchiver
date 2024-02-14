from PIL import Image
import math

img = Image.open("test.jpg")
image_x = img.width
image_y = img.height

resize_x = 100

# 最大公約数を求め、アスペクト比を計算する
gcdevi = math.gcd(image_x, image_y)
aspect = (image_x // gcdevi, image_y // gcdevi)

# アスペクト比を元に、リサイズ後のサイズを計算する
size = (image_x // aspect[0], image_y // aspect[1])

img_resized = img.resize(size)

img_resized.save("test_resized.jpg")