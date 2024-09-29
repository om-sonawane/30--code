from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk
import tkinter as tk

# main Class
class main:
    def __init__(self, master):
        # Window
        self.master = master
        # Useful variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.n_username = tk.StringVar()
        self.n_password = tk.StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find user
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                       "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            msg = ""
            self.logf.pack_forget()
            ms.showinfo("Success", "Login successful!")
            root.destroy()
            # Uncomment the below to call another script on successful login
            # from subprocess import call
            # call(['python', 'GUI_master.py'])
        else:
            ms.showerror('Error', 'Username or password did not match.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Check for existing username
        find_user = ('SELECT * FROM admin_registration WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error', 'Username taken, try a different one.')
        else:
            insert = 'INSERT INTO admin_registration(username,password) VALUES(?,?)'
            c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
            db.commit()
            ms.showinfo('Success', 'Account created successfully!')
            self.log()

    # Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Widgets Design
    def widgets(self):
        # Header label with modern font and golden background
        self.head = tk.Label(self.master, text='Welcome to Login', background="#f7e0f4", font=('Helvetica', 24, 'bold'),
                             pady=20, fg="#333")
        self.head.pack()

        # Login Frame
        self.logf = tk.Frame(self.master, padx=50, pady=20, background="#FFE5EC")
        
        tk.Label(self.logf, text='Username: ', background="#FFE5EC", font=("Helvetica", 18), pady=5,
                 padx=5, fg="#333").grid(sticky=tk.W)
        tk.Entry(self.logf, textvariable=self.username, bd=5, background="white", font=('', 15)).grid(row=0, column=1)

        tk.Label(self.logf, text='Password: ', background="#FFE5EC", font=("Helvetica", 18), pady=5,
                 padx=5, fg="#333").grid(sticky=tk.W)
        tk.Entry(self.logf, textvariable=self.password, bd=5, background="white", font=('', 15), show='*').grid(row=1,
                                                                                                                column=1)
        tk.Button(self.logf, text=' Login ', command=self.login, bd=3, font=("Helvetica", 16), background="#FF69B4",
                  foreground="white", padx=5, pady=5).grid(row=2, column=0, pady=10)
        
        tk.Button(self.logf, text=' Create Account ', command=self.cr, bd=3, font=("Helvetica", 16), background="#FFD700",
                  foreground="white", padx=5, pady=5).grid(row=2, column=1, pady=10)

        self.logf.pack()

        # Create Account Frame
        self.crf = tk.Frame(self.master, padx=50, pady=20, background="#FFE5EC")
        tk.Label(self.crf, text='New Username: ', background="#FFE5EC", font=("Helvetica", 18), pady=5,
                 padx=5, fg="#333").grid(sticky=tk.W)
        tk.Entry(self.crf, textvariable=self.n_username, bd=5, background="white", font=('', 15)).grid(row=0, column=1)

        tk.Label(self.crf, text='New Password: ', background="#FFE5EC", font=("Helvetica", 18), pady=5,
                 padx=5, fg="#333").grid(sticky=tk.W)
        tk.Entry(self.crf, textvariable=self.n_password, bd=5, background="white", font=('', 15), show='*').grid(row=1,
                                                                                                                 column=1)
        tk.Button(self.crf, text='Create Account', command=self.new_user, bd=3, font=("Helvetica", 16),
                  background="#FF69B4", foreground="white", padx=5, pady=5).grid(row=2, column=0, pady=10)

        tk.Button(self.crf, text='Back to Login', command=self.log, bd=3, font=("Helvetica", 16),
                  background="#FFD700", foreground="white", padx=5, pady=5).grid(row=2, column=1, pady=10)

# Main window setup
root = tk.Tk()
root.configure(background="#FFE5EC")  # Light pastel pink background
root.geometry("500x400")
root.title("Login")

# Start the application
main(root)
root.mainloop()
