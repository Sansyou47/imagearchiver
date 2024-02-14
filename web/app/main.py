from PIL import Image

img = Image.open("test.jpg")

(width, height) = (img.width // 2, img.height // 2)

img_resized = img.resize((width, height))

img_resized.save("test_resized.jpg")