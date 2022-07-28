from PIL import Image, ImageEnhance
import os

im = Image.open("logo.png")

box = (0, 28, 128, 100)
logo = im.crop(box)

directory = 'Pictures'

for filename in os.listdir(directory):
    try:
        path = os.path.join(directory, filename)
        image = Image.open(path)
        size_tuple = image.size
        original_height = size_tuple[0]
        proportion = 1000 / original_height
        new_width = int(proportion * size_tuple[1])
        resized_image = image.resize((1000, new_width))
        resized_image.paste(im, (872, new_width - 100), im)
        resized_image.show()
    except IOError:
        continue