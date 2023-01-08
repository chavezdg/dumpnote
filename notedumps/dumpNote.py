#!/usr/bin/env python3

# DUMP NOTE
# Version: 1.0
# Release Date: 1/2/23
# Author: davidc
# Dump Note is a Python plus tKinter program
# used as a note taking tool that puts your notes
# in one central location.

'''
Copyright (c) 2023, David Geovanny Chavez

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from tkinter import *
from PIL import ImageTk,Image
import os, re, subprocess
from tkinter import font
from index_list import *
from editThisNote import *
from profile import *


specialK = re.compile('[@_!#$&%^%*()<>?/\|}{~:+-]')
profile_width = str(profile_width)
profile_length = str(profile_length)


def dump_function():
 global index   
 global note_title 
 global note_details
 note_title = noteEntryString.get()
 note_details = notePad.get("1.0", "end-1c")

 if len(note_title) == 0:
  print("ERROR: No title included as a header error. A title of at least 1 character is needed to dump a note.")
 elif specialK.search(note_title) != None:
  print("ERROR: No special characters in title are to be included to dump a note")
 elif note_title in index:
  print(os.system("date"))
  print(note_title + " appended")
  print(note_details)
  os.popen("echo \'" + note_details + "\' >> " + "index/\'" + note_title + "\'")
  noteEntry.delete(0, 'end')
  notePad.delete("1.0", "end-1c")
 else:
  print(os.system("date"))
  os.system("echo \'" + note_title + "\' > title.txt")
  os.system("./index_append.sh")
  print(index)
  print("Add " + note_title + " to note index")
  print(note_details)
  os.popen("touch index/\'" + note_title + "\'")
  os.popen("chmod 755 index/\'" + note_title + "\'")
  os.popen("echo \'" + note_details + "\' >> " + "index/\'" + note_title + "\'")
  noteEntry.delete(0, 'end')
  notePad.delete("1.0", "end-1c")


def notes_function():
 gui.destroy()
 os.system("python3 viewNotes.py")


def recycle_function():
 os.system("python3 recycleNotes.py")


def default_sel():
 os.popen("echo \"profile_user=\'user\'\" > profile.py")
 os.popen("echo \"profile_font=\'Ubuntu Mono\'\" >> profile.py")
 os.popen("echo 'profile_width=570' >> profile.py")
 os.popen("echo 'profile_length=690' >> profile.py")
 os.popen("echo \"profile_online=\'OFF\'\" >> profile.py") 
 print("DEFAULT PROFILE SELECTED.")
 profile_gui.destroy()
 gui.destroy()
 os.system("python3 dumpNote.py")


# This is for online recycling.
def isChecked():
 pass


def ok_sel():
 ok_user = username_entry.get()
 ok_font = font_sel.get()
 ok_width = str(width.get())
 ok_length = str(length.get())
 online_checkerVar.set("OFF")
 ok_online= online_checkerVar.get()

 os.popen("echo \"profile_user=\'" + ok_user + "\'\" > profile.py")
 os.popen("echo \"profile_font=\'" + ok_font + "\'\" >> profile.py")
 os.popen("echo 'profile_width=" + ok_width + "' >> profile.py")
 os.popen("echo 'profile_length=" + ok_length + "' >> profile.py")
 os.popen("echo \"profile_online=\'" + ok_online + "\'\" >> profile.py") 
 print("USER PROFILE UPDATED.")
 profile_gui.destroy()
 gui.destroy()
 os.system("python3 dumpNote.py")


def profile():
 global profile_gui
 profile_gui = Tk()
 profile_gui.title('PROFILE')
 profile_gui.geometry("500x555")

 global username_entry
 global font_sel
 global width
 global length
 global online_checkerVar
 
 user_str = StringVar()
 username_frame = LabelFrame(profile_gui, text="USERNAME", font=(profile_font, 12), padx=5, pady=5)
 username_entry = Entry(username_frame)
 username_entry.insert(0, profile_user)
 username_entry.pack()
 username_frame.pack()
 
 font_frame = LabelFrame(profile_gui, text="FONT", font=(profile_font, 12), padx=5, pady=5)
 font_list = font.families()
 font_list = ["Ani", "C059", "Chandas", "Courier", "Courier 10 Pitch", "DejaVu Sans", "FreeMono", \
              "Gargi", "Garuda", "Karumbi", "Lato", "Liberation Serif", "Lohit Assamese", "Loma", \
              "Nakula", "Noto Sans Mono", "Noto Sans Wancho", "Noto Serif", "Noto Mono", "Saab", \
              "Rasa", "Ubuntu", "Ubuntu Mono", "Vemana2000", "Waree", "Yrsa", "Z003"]
 font_sel = StringVar(font_frame)
 font_sel.set(profile_font)
 font_source = OptionMenu(font_frame, font_sel, *font_list)
 font_source.pack()
 font_frame.pack()

 window_size_frame = LabelFrame(profile_gui, text="DEFAULT APP WINDOW SIZE", font=(profile_font, 12), padx=5, pady=5)
 label_scale = Label(window_size_frame, text="WxL=", font=(profile_font, 12))
 width_str = str(profile_width)
 length_str = str(profile_length)
 width = Scale(window_size_frame, from_=560, to=800, orient=HORIZONTAL)
 length = Scale(window_size_frame, from_=660, to=800)
 c_label_scale = Label(window_size_frame, text="" + width_str + "x" + length_str)
 label_scale.grid(row=0, column=0)
 c_label_scale.grid(row=0, column=1)
 width.grid(row=1, column=1)
 length.grid(row=0, column=2)
 window_size_frame.pack()

 recycle_frame = LabelFrame(profile_gui, text="RECYCLE NOTES", font=(profile_font, 12), padx=5, pady=5)
 recycle_online_label = Label(recycle_frame, text="online  ", font=(profile_font, 12))
 online_checkerVar = StringVar()
 online_checker = Button(recycle_frame, text=profile_online) #, command=isChecked?)
 online_checker["state"] = "disabled"
 recycle_online_label.grid(row=0, column=0)
 online_checker.grid(row=0, column=1)
 recycle_frame.pack()

 pro_sel_frame = LabelFrame(profile_gui, text="CONFIRM SELECTION", font=(profile_font, 12), padx=5, pady=5)
 default_btn = Button(pro_sel_frame, text="DEFAULT", font=(profile_font, 12), padx=1, pady=1, command=default_sel)
 default_space_label = Label(pro_sel_frame, text="        ")
 ok_btn = Button(pro_sel_frame, text="OK", font=(profile_font, 12), padx=10, pady=10, command=ok_sel)
 default_btn.grid(row=0, column=0)
 default_space_label.grid(row=0, column=1)
 ok_btn.grid(row=0, column=2)
 pro_sel_frame.pack()


def about_function():
 os.system("python3 noteAbout.py")


def help_function():
 os.system("python3 noteHelp.py")


class MenuBar(Menu):

 def __init__(self, gui):
  Menu.__init__(self, gui)

  note = Menu(self, tearoff=False)
  self.add_cascade(label="Menu", underline=0, font=(profile_font, 12), menu=note)
  note.add_command(label="Dump", underline=0, font=(profile_font, 12), command=dump_function)
  note.add_command(label="Notes", underline=1, font=(profile_font, 12), command=notes_function)
  note.add_command(label="Recycle", underline=0, font=(profile_font, 12), command=recycle_function)
  note.add_separator()
  note.add_command(label="Profile", underline=0, font=(profile_font, 12), command=profile)
  note.add_separator()
  note.add_command(label="About", underline=0, font=(profile_font, 12), command=about_function)
  note.add_command(label="Help", underline=0, font=(profile_font, 12), command=help_function)
  note.add_command(label="Exit", underline=0, font=(profile_font, 12), command=quit)

class MenuD(Tk):
 def __init__(self):
     Tk.__init__(self)
     menubar = MenuBar(self)
     self.config(menu=menubar)


if __name__ == "__main__":
    
    # GUI variables.
    gui = MenuD()
    gui.title('DUMP NOTE')
    gui.geometry('' + profile_width + 'x' + profile_length + '')
    gui_frame = LabelFrame(gui, padx=5, pady=5)

    # Note option frame.
    note_option_frame = LabelFrame(gui_frame, padx=5, pady=5)
    dump_note = Button(note_option_frame, text="Dump", underline=0, font=(profile_font, 12), command=dump_function)

    # Notepad variables.
    note_frame = LabelFrame(gui_frame, padx=5, pady=5, font=('Ubuntu bold',16))
    noteEntryString = StringVar()
    noteEntry = Entry(note_frame, textvariable=noteEntryString, font=(profile_font, 12), show="", bg="light yellow")
    notePad = Text(note_frame, font=(profile_font, 12), height=25, width=50, bg="light yellow")
    
    if indexName != "":
     noteEntryString.set(indexName)
     notePad.insert(INSERT, "" + os.popen("cat index/" + "\'" + indexName + "\'").read())

    # Selection variables.
    select_frame = LabelFrame(note_frame, padx=5, pady=5)
    notes_directory = Button(select_frame, text="Notes", underline=1, font=(profile_font, 12), padx=1, pady=1, command=notes_function)
    
    # Placement of things..
    dump_note.pack()
    note_option_frame.pack()
    noteEntry.pack()
    notePad.pack()
    notes_directory.grid(row=0, column=1)
    select_frame.pack()
    note_frame.pack()
    gui_frame.pack()
    gui.mainloop()



