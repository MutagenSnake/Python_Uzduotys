from PIL import Image

sample = "Pictures/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg"

def return_valid(number):
    if number > 255:
        return 255
    elif number < 0:
        return 0
    else:
        return number

def modify_color(original_tuple, input_tuple):
    red = return_valid(original_tuple[0] + input_tuple[0])
    green = return_valid(original_tuple[1] + input_tuple[1])
    blue = return_valid(original_tuple[2] + input_tuple[2])
    new_tuple = (red, green, blue)
    return new_tuple

def modify_image(image, red=0, green=0, blue=0):
    work_image = Image.open(image)
    raw_data = work_image.getdata()
    final_data = []
    for tuple in raw_data:
        new_tuple = modify_color(tuple, (red, green, blue))
        final_data.append(new_tuple)
    work_image.putdata(final_data)
    work_image.show()

modify_image(sample, 150, 0, 0)