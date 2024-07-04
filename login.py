import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import *
from customtkinter import *

def validate_login():
    email = email_entry.get()
    password = password_entry.get()
    
    # Basic validation
    if email == "try@mail" and password == "123":
        import mini_project_front_end
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")


root = Tk()
root.title("Login")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.state('zoomed')
root.geometry("1580x850")   #uss upar ke set height width se screen full cover nhi karra @domi
root.configure(bg="#0F141E")  # Set background color

# just some labels..ignore.@domi
header_label = Label(root, text="ResuCraft", font=("Helvetica", 40, "bold"), bg="#0F141E",fg="#4AD0D7")
header_label.place(x=790,y=60, anchor="center")
header_labe2 = Label(root, text="Just a step before we generate a specially curated Resume,JUST for you !!!", font=("Helvetica", 15, "bold"), bg="#0F141E",fg="#FFFFFF")
header_labe2.place(x=800,y=100, anchor="center")

# frame made for border @domi
bd_frame=Frame(master=root,height=550,width=470,bg='#4AD0D7')
bd_frame.place(x=560,y=160,)

# main content frame...@domi
main_frame=Frame(master=bd_frame,height=540,width=460,bg='#0F141E')
main_frame.place(x=5,y=5)

l1=Label(master=main_frame,text="LOGIN",fg='#E3D74A',bg='#0F141E',font=("Noto Sans CJK SC", 30, "bold"))
l1.place(x=160,y=40)

email_label = Label(main_frame, text="Email :", font=("Noto Sans CJK SC", 25), bg="#0F141E",fg='white')
email_label.place(x=30,y=160)

# email entry idhar... @domi
email_entry = Entry(main_frame, font=("Noto Sans CJK SC", 20), bg="#2C323E",fg='#E3D74A', relief="solid", bd=1)
email_entry.place(x=140,y=165)

password_label = Label(main_frame, text="UID :",font=("Noto Sans CJK SC", 25), bg="#0F141E",fg='white' )
password_label.place(x=30,y=280)

#password entry idhar...@domi
password_entry = Entry(main_frame, font=("Noto Sans CJK SC", 20), bg="#2C323E",fg='#E3D74A', relief="solid", bd=1)
password_entry.place(x=140,y=285)

# @dev...validate login credentilas from data base using this button func
login_button = Button(main_frame, text="Login", command=validate_login, font=("Noto Sans CJK SC", 20), bg="#192130", fg="#4AD0D7", relief="raised")
login_button.place(x=140,y=380)

back_button=Button(main_frame, text="⬅", font=("Noto Sans CJK SC", 20), bg="#192130", fg="#4AD0D7",command=root.destroy).place(x=290, y=380)

root.mainloop()