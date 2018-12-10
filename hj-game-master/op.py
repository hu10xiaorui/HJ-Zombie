import tkinter
from tkinter.colorchooser import askcolor
from tkinter.constants import *
import sys

def menu():
    import os
    os.system("python3 main.py")

def callback():
    fileName = askcolor()
    with open("color", "w") as sc2:
        sc2.write(str(fileName[0]))
'''
    tk.title("SETTINGS")
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)
    label = tkinter.Label(frame, text="COLOR SETTED!!!")
    label.pack(fill=X, expand=1)
    button2 = tkinter.Button(frame, text="EXIT", command=tk.destroy)
    button2.pack(side=BOTTOM)
    button5 = tkinter.Button(frame, text="MENU", command=menu)
    button5.pack(side=BOTTOM)
'''

tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
tk.title("SETTINGS")
label = tkinter.Label(frame, text="BACKGROUND COLOR")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame, text="SET COLOR", command=callback)
button.pack(side=BOTTOM)
button2 = tkinter.Button(frame, text="EXIT", command=tk.quit)
button2.pack(side=BOTTOM)
#button5 = tkinter.Button(frame, text="MENU", command=menu)
#button5.pack(side=BOTTOM)
tk.mainloop()