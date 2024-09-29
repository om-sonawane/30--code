# -*- coding: utf-8 -*-
import sqlite3
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from subprocess import call

root = tk.Tk()

# Setting full-screen dimensions
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Efficient Software Defects Prediction using SVM")

# Configure background color for a cleaner look
root.configure(background="#FFF5F5")  # Soft, off-white pastel

# Function to open registration page
def reg():
    print("Opening Registration")
    call(["python", "registration.py"])

# Function to open login page
def login():
    print("Opening Login")
    call(["python", "login.py"])

# Set background image
image2 = Image.open('sample.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Title label with updated styling
lbl = tk.Label(root, text="Efficient Software Defects Prediction using SVM", 
               font=('Helvetica', 36, 'bold'), height=2, bg="#344955", fg="white", relief=tk.RAISED)
lbl.pack(fill=tk.X)

# Frame for the Login and Register buttons
framed = tk.LabelFrame(root, text="Welcome", width=550, height=300, bd=3, 
                       font=('Helvetica', 18, 'bold'), bg="#4A6572", fg="white", relief=tk.GROOVE)
framed.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Modernized buttons with rounded edges and hover effects
style_button = {
    'font': ('Helvetica', 16, 'bold'),  
    'bg': '#fdbafd',   # Attractive pastel pink tone
    'fg': 'white',
    'activebackground': '#FF6F00',  # Darker shade for hover
    'activeforeground': 'white',
    'bd': 3,
    'relief': tk.RAISED,
    'width': 15,
    'height': 2
}

# Login button (left-aligned within the frame)
login_button = tk.Button(framed, text='Login Now', command=login, **style_button)
login_button.place(relx=0.3, rely=0.5, anchor=tk.CENTER)  # Adjusted position to 0.3

# Register button (right-aligned with space in between)
register_button = tk.Button(framed, text='Register', command=reg, **style_button)
register_button.place(relx=0.7, rely=0.5, anchor=tk.CENTER)  # Adjusted position to 0.7
root.mainloop()
