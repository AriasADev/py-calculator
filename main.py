import sys
import os
from tkinter import *

def enforce_aspect(event):
    if event.widget == root:
        w, h = root.winfo_width(), root.winfo_height()
        if w / h != aspect_ratio:
            root.geometry(f"{int(h * aspect_ratio)}x{h}" if w > h * aspect_ratio else f"{w}x{int(w / aspect_ratio)}")

def calculator():
    global root, aspect_ratio
    root = Tk()
    aspect_ratio = 3 / 4
    root.title("Calculator")
    root.geometry("300x400")
    root.minsize(300, 400)

    # Handle icon for bundled executable
    if getattr(sys, 'frozen', False):  # If running as a bundled executable
        icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
    else:  # If running as a script
        icon_path = 'icon.ico'

    try:
        root.iconbitmap(default=icon_path)
    except Exception as e:
        print(f"Error loading icon: {e}")

    root.bind("<Configure>", enforce_aspect)
    
    label = Label(root, text="Welcome to the Calculator!\nTest")
    label.pack()

    root.mainloop()

calculator()
