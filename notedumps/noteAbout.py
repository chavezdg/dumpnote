#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk, Image

about_gui = Tk()
about_gui.title('ABOUT')
about_gui.geometry("750x550")

about_gui_frame = LabelFrame(about_gui, padx=5, pady=5)
image_frame = LabelFrame(about_gui_frame, padx=5, pady=5)
text_frame = LabelFrame(about_gui_frame, padx=5, pady=5)

image=Image.open('images/help_00.png')
img=image.resize((450, 350))
about_img=ImageTk.PhotoImage(img)
img_label=Label(about_gui_frame, image=about_img)

about_text_label = Label(text_frame, text="\
DUMP NOTE \n \
Version: 1.0 \n \
Release Date: 1/2/23 \n \
\n \
Dump Note is a text editor for fast workflow. \n \
Visit notelinkshare.com for more information. \n \
Created by davidc.")

img_label.pack()
about_text_label.pack()

image_frame.pack()
text_frame.pack()
about_gui_frame.pack()

about_gui.mainloop()


