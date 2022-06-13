from tkinter import *
from PIL import ImageTk, Image
import os

file_list = os.listdir('Pictures')
list_len = len(file_list)

main_window = Tk()
main_window.title('Picture browser')
main_window.iconbitmap('image-files.ico')

current_image = 0
image_for_display = ImageTk.PhotoImage(Image.open(f'Pictures/{file_list[current_image]}'))

image_label = Label(image=image_for_display)
image_label.grid(row=0, column=0, columnspan=3)

def forward():
    global current_image
    global image_label
    global image_for_display
    image_label.grid_forget()
    if current_image + 1 < list_len:
        current_image += 1
    else:
        pass
    image_for_display = ImageTk.PhotoImage(Image.open(f'Pictures/{file_list[current_image]}'))
    image_label = Label(image=image_for_display)
    image_label.grid(row=0, column=0, columnspan=3)

def back():
    global current_image
    global image_label
    global image_for_display
    image_label.grid_forget()
    if current_image > 0:
        current_image -= 1
    else:
        pass
    image_for_display = ImageTk.PhotoImage(Image.open(f'Pictures/{file_list[current_image]}'))
    image_label = Label(image=image_for_display)
    image_label.grid(row=0, column=0, columnspan=3)


back_button = Button(main_window, text="<<<", command=back)
forward_button = Button(main_window, text=">>>", command=forward)

back_button.grid(row=1, column=0)
forward_button.grid(row=1, column=2)

main_window.mainloop()

