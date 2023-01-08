#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk, Image

help_gui = Tk()
help_gui.title('HELP')
help_gui.geometry("750x550")

help_gui_frame = LabelFrame(help_gui, padx=5, pady=5)
image_frame = LabelFrame(help_gui_frame, padx=5, pady=5)
text_frame = LabelFrame(help_gui_frame, padx=5, pady=5)

image=Image.open('images/help_2.png')
img=image.resize((450, 350))
help_img=ImageTk.PhotoImage(img)
img_label=Label(help_gui_frame, image=help_img)

help_text_label = Label(text_frame, text="\
Write a title on the Title field. \n \
The title is also the filename of the note.\n \
No special characters and at least one character is needed to save a note.\n \
Writing your note without a title is not an acceptable dump of a note.\n \
Save your notes by clicking on the Dump button above the title field. \n \
View your notes by clicking on the Notes button below the notepad field. \n \
To recycle your notes, click on the Menu and select Recycle. \n \
For online software service and support, go to www.notelinkshare.com")

img_label.pack()
help_text_label.pack()

image_frame.pack()
text_frame.pack()
help_gui_frame.pack()

help_gui.mainloop()


