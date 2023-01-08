#!/usr/bin/env python3

# RECYCLE NOTES
# Version 1.0
# Release Date: 1/2/23
# Author: davidc
# Recycle Notes is a Python w/ tKinter program that you could
# use to recycle the notes you dumped in the dump notes program.
# The files the notes are on are not destroyed; the user
# must manually destroy the files that are in the recycle folder.

'''
Copyright (c) 2023, David Geovanny Chavez

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from tkinter import *
import os, re, subprocess
from PIL import ImageTk, Image
from index_list import *
from profile import *


guiv = Tk()
guiv.title('RECYCLE NOTES')
profile_width = str(profile_width)
profile_length = str(profile_length)
guiv.geometry('' + profile_width + 'x' + profile_length + '')
bgimg = Image.open('images/recycle.png')
bgimg = bgimg.resize((50, 50))
bgimg = ImageTk.PhotoImage(bgimg)
bgimg_label = Label(guiv, i=bgimg)

file_directory_frame = Label(guiv, text="" + os.popen("pwd").read() + "/index", font=(profile_font, 12))
bgimg_label.pack()
file_directory_frame.pack()

print("RECYCLE NOTES")
print(index)
iVarNo = -1
indexVar = index[iVarNo]
indexVar_note = os.popen("cat index/" + "\'" + indexVar + "\'").read()


def back_function():
 global iVarNo
 global indexVar
 global indexVar_note

 iVarNo = iVarNo - 1
 indexVar = index[iVarNo]
 indexVar_note = os.popen("cat index/" + "\'" + indexVar + "\'").read()
 gui_frame.destroy()
 note_frame.destroy()
 button_frame.destroy()
 post_notes_data = Notes(guiv)


def note_function():
 global iVarNo
 global indexVar
 global indexVar_note

 indexVar_note = os.popen("mv index/" + "\'" + indexVar + "\'" + " local_dump/").read()
 index.remove(indexVar)
 os.popen("echo \"index = " + str(index) + "\" > index_list.py").read()
 print("REMOVED " + indexVar + " FROM INDEX")
 print(index)
 gui_frame.destroy()
 note_frame.destroy()
 button_frame.destroy()
 iVarNo = -1
 indexVar = index[iVarNo]
 indexVar_note = os.popen("cat index/" + "\'" + indexVar + "\'").read()
 post_notes_data = Notes(guiv)


def next_function():
 global iVarNo
 global indexVar
 global indexVar_note

 iVarNo = iVarNo + 1
 indexVar = index[iVarNo]
 indexVar_note = os.popen("cat index/" + "\'" + indexVar + "\'").read()
 gui_frame.destroy()
 note_frame.destroy()
 button_frame.destroy()
 post_notes_data = Notes(guiv)


class Notes:

 def __init__(self, master):
  global gui_frame
  global note_frame
  global button_frame

  gui_frame = LabelFrame(master, padx=10, pady=10)
  note_frame = LabelFrame(gui_frame, padx=5, pady=5)
  button_frame = LabelFrame(gui_frame, padx=5, pady=5)
  gui_frame.pack()
  button_frame.pack()
  note_frame.pack()


  note_view = Label(note_frame, text=indexVar_note, font=(profile_font, 12), padx=5, pady=5)
  note_view.pack()

  self.back_button = Button(button_frame, text="BACK", font=(profile_font, 12), underline=0, command=back_function)
  self.note_button = Button(button_frame, text=indexVar, font=(profile_font, 12), command=note_function)
  self.next_button = Button(button_frame, text="NEXT", font=(profile_font, 12), underline=0, command=next_function)

  if len(index) == 1:
   print("NO NOTES TO RECYCLE")
   self.note_button = Button(button_frame, text=indexVar, font=(profile_font, 12), state=DISABLED)

  if indexVar == index[0]:
   self.back_button = Button(button_frame, text="BACK", font=(profile_font, 12), state=DISABLED)

  if indexVar == index[-1]:
   self.next_button = Button(button_frame, text="NEXT", font=(profile_font, 12), state=DISABLED)

  self.back_button.grid(row=0, column=0)
  self.note_button.grid(row=0, column=1)
  self.next_button.grid(row=0, column=2)



post_notes_data = Notes(guiv)


guiv.mainloop()


