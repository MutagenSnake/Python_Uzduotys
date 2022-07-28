from PIL import Image, ImageEnhance

im = Image.open("logo.png")

box = (0, 28, 128, 100)
crop_im = im.crop(box)

def modify_image(image, contrast = 100, color = 100 , brightness = 100, save_y_or_n = 'n'):
    im = Image.open(image)
    # contrast
    enhancer_contrast = ImageEnhance.Contrast(im)
    factor_con = contrast/100
    im_con = enhancer_contrast.enhance(factor_con)
    # color
    enhancer_color = ImageEnhance.Color(im_con)
    factor_col = color / 100
    im_col = enhancer_color.enhance(factor_col)
    # brightness
    enhancer_brightness = ImageEnhance.Brightness(im_col)
    factor_bri = brightness / 100
    im_bri = enhancer_brightness.enhance(factor_bri)
    # aux
    if save_y_or_n == 'y':
        image_split_list = image.split('.')
        im_bri.save(f'{image_split_list[0]}_modified.{image_split_list[1]}')
        im_bri.show()
    else:
        im_bri.show()

# modify_image('shuo.png', 150, 150, 150, 'y')

