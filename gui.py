import sys
import os
import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title("JOSH - Voice-Controlled A.I Assistant")

frame=tk.Frame(window)
frame.pack()

def hellojosh():
	os.system('python3 main.py')

def facialscan():
	os.system('python3 faces.py')

#def add_dataset():
#	os.system('python3 build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/')

L1=tk.Label(frame, text="Welcome to Your Very Own Artificially Intelligent House Assistant", fg="blue")
L1.pack(side="top")

B1=tk.Button(frame, text="Talk to Josh", command= hellojosh)
B1.pack(side="left")

B2=tk.Button(frame, text="open camers", command= facialscan)
B2.pack(side="right")

B3=tk.Button(frame, text="QUIT", fg="red", command= quit)
B3.pack(side="bottom")

#B4=tk.Button(frame, text="Add Dataset", command= add_dataset)
#B4.pack(side="bottom")

window.mainloop()
