from PIL import Image

black_tuple = (0,0,0)
white_tuple = (255, 255, 255)
image = Image.open("Pictures/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg")
starting_image_data = image.getdata()

red_max = 100
green_max = 100
blue_max = 100

final_image_data = []
for tuple in starting_image_data:
    if tuple[0] >= red_max or tuple[1] >= green_max or tuple[2] >= green_max:
        final_image_data.append(white_tuple)
    else:
        final_image_data.append(black_tuple)

image.putdata(final_image_data)
image.show()