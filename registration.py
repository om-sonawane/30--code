import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random

# Create window
window = tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="#FFE5EC")  # Light pastel pink background to match main UI

# Variables
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()  # Gender (1 for male, 2 for female)
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
value = random.randint(1, 1000)
print(value)

# Database setup
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()

# Password validation function
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True
    if len(passwd) < 6:
        val = False
    if len(passwd) > 20:
        val = False
    if not any(char.isdigit() for char in passwd):
        val = False
    if not any(char.isupper() for char in passwd):
        val = False
    if not any(char.islower() for char in passwd):
        val = False
    if not any(char in SpecialSym for char in passwd):
        val = False
    return val

# Insert into the database
def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    # Regex for email
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
    find_user = 'SELECT * FROM admin_registration WHERE username = ?'
    c.execute(find_user, [(username.get())])

    # Validation
    if fname.isdigit() or fname == "":
        ms.showerror("Error", "Please enter a valid name")
    elif addr == "":
        ms.showerror("Error", "Please enter an address")
    elif email == "" or not re.search(regex, email):
        ms.showerror("Error", "Please enter a valid email")
    elif len(str(mobile)) != 10:
        ms.showerror("Error", "Please enter a 10-digit mobile number")
    elif time > 100 or time == 0:
        ms.showerror("Error", "Please enter a valid age")
    elif c.fetchall():
        ms.showerror("Error", "Username taken, please try a different one")
    elif not password_check(pwd):
        ms.showerror("Error", "Password must contain at least 1 uppercase letter, 1 symbol, and 1 number")
    elif pwd != cnpwd:
        ms.showerror("Error", "Password and confirm password must match")
    elif gender not in [1, 2]:
        ms.showerror("Error", "Please select gender")
    else:
        cursor.execute(
            'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age, password) VALUES(?,?,?,?,?,?,?,?)',
            (fname, addr, un, email, mobile, gender, time, pwd))
        db.commit()
        ms.showinfo('Success!', 'Account Created Successfully!')
        window.destroy()

# Background image
image2 = Image.open('sample.jpg')
image2 = image2.resize((700, 700), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Widgets
l1 = tk.Label(window, text="Registration Form", font=("Helvetica", 30, "bold"), bg="#FFB6C1", fg="black")  # Pastel Pink heading
l1.place(x=190, y=50)

tk.Label(window, text="Full Name:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=150)
tk.Entry(window, textvar=Fullname, width=25, font=('', 12)).place(x=330, y=150)

tk.Label(window, text="Address:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=200)
tk.Entry(window, textvar=address, width=25, font=('', 12)).place(x=330, y=200)

tk.Label(window, text="E-mail:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=250)
tk.Entry(window, textvar=Email, width=25, font=('', 12)).place(x=330, y=250)

tk.Label(window, text="Phone number:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=300)
tk.Entry(window, textvar=Phoneno, width=25, font=('', 12)).place(x=330, y=300)

tk.Label(window, text="Gender:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=350)
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="#FFE5EC", font=("Helvetica", 12), variable=var, value=1).place(x=330, y=350)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="#FFE5EC", font=("Helvetica", 12), variable=var, value=2).place(x=440, y=350)

tk.Label(window, text="Age:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=400)
tk.Entry(window, textvar=age, width=25, font=('', 12)).place(x=330, y=400)

tk.Label(window, text="User Name:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=450)
tk.Entry(window, textvar=username, width=25, font=('', 12)).place(x=330, y=450)

tk.Label(window, text="Password:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=500)
tk.Entry(window, textvar=password, width=25, font=('', 12), show="*").place(x=330, y=500)

tk.Label(window, text="Confirm Password:", font=("Helvetica", 14), bg="#FFE5EC", fg="#444").place(x=130, y=550)
tk.Entry(window, textvar=password1, width=25, font=('', 12), show="*").place(x=330, y=550)

tk.Button(window, text="Register", bg="#FF69B4", font=("Helvetica", 16), fg="white", command=insert).place(x=270, y=620)

# Start the window loop
window.mainloop()