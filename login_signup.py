from tkinter import *
import os
import database as db 

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3,text="Login Success").pack()
    Button(screen3,text="OK", width=10, height=1, command= delete2).pack()
    screen2.destroy()
    screen.destroy()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Failure")
    screen4.geometry("150x100")
    Label(screen4,text="Password Not Recognised!").pack()
    Button(screen4, text="OK", width=10, height=1, command= delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Failure")
    screen5.geometry("150x100")
    Label(screen5,text="User Not Found").pack()
    Button(screen5, text="OK", width=10, height=1, command= delete4).pack()

def register_user():
    global invalid_msg
    username_info = username.get()
    password_info = password.get()
    name_info = name.get()
    if(name_info and username_info and password_info):
        db.createUser(name_info, username_info, password_info)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        if(invalid_msg):
            invalid_msg.destroy()
        Label(screen1, text = "Registration Success", fg="green", font= ("Calibri", 11)).pack()
    else:
        invalid_msg = Label(screen1, text = "Invalid Inputs", fg="red", font= ("Calibri", 11))
        invalid_msg.pack()
    

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    user = db.login(username1, password1)
    if user:
        login_success()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global name
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    name = StringVar()

    Label(screen1,text="Please Enter Details Below").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username *").pack()
   
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Name *").pack()
    name_entry = Entry(screen1,textvariable=name)
    name_entry.pack()
    Label(screen1,text="Password *").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register", width=10, height=1, command= register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter the details below to Login").pack()
    Label(screen2,text="").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2,text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable= username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable= password_verify)
    password_entry1.pack()
    Button(screen2,text="Login", width=10, height=1, command= login_verify).pack()



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Tiles Game")
    Label(text="TILES", bg = "grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command= login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command= register).pack()

    screen.mainloop()
