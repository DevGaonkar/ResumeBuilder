from tkinter import *
import sqlite3

# Database code
conn = sqlite3.connect('auth.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE USERS (
          NAME TEXT,
          EMAIL TEXT,
          PASSWORD TEXT
    )""")
    conn.commit()
except sqlite3.OperationalError:
    pass


def signupbut():
    name = namelog.get()
    email = emaillog.get()
    passwrd = password.get()
    c.execute("INSERT INTO USERS VALUES (?,?,?)", (name, email, passwrd))
    conn.commit()
    loginwin.destroy()


def login():
    print("Login button clicked")
    import login

def main():
    print("Back button clicked")
    import canvas

loginwin = Tk()
loginwin.state('zoomed')
loginwin.title("Sign Up - ResumeBuilder")   

loginwin.configure(bg="#0F141E")

header_label = Label(loginwin, text="ResuCraft", font=("Arial", 40, "bold"), fg="#4AD0D7",bg='#0F141E')
header_label.place(x=670,y=30)

h1=Label(loginwin,text="Welcome aboard! 🚀.Your journey with us is about to begin.",font=("Arial", 20, "bold"),bg='#0F141E',fg="#976fad")
h1.place(x=400,y=90)

h2=Label(loginwin,text="First things first ,Let's start by Signing Up",font=("Arial", 20, "bold"),bg='#0F141E',fg="white")
h2.place(x=520,y=170)

#faltu frame..used for border..@domi
bd_frame=Frame(master=loginwin,height=550,width=470,bg='#4AD0D7')
bd_frame.place(x=560,y=210,)

#main frame
main_frame=Frame(master=bd_frame,height=540,width=460,bg='#0F141E')
main_frame.place(x=5,y=5)

l1=Label(master=main_frame,text="Sign-Up",fg='#E3D74A',bg='#0F141E',font=("Noto Sans CJK SC", 40, "bold"))
l1.place(x=140,y=40)

name_label = Label(main_frame, text="Name :", font=("Noto Sans CJK SC", 25), bg="#0F141E",fg='white')
name_label.place(x=30,y=160)

email_label = Label(main_frame, text="Email :", font=("Noto Sans CJK SC", 25), bg="#0F141E",fg='white')
email_label.place(x=30,y=260)

password_label = Label(main_frame, text="UID :",font=("Noto Sans CJK SC", 25), bg="#0F141E",fg='white' )
password_label.place(x=30,y=360)

# name ka input idhar aayega.......ye personal details mai bhi use hoga..@domi
namelog = Entry(main_frame, font=("Noto Sans CJK SC", 20), bg="#2C323E",fg='#E3D74A', relief="solid", bd=1)
namelog.place(x=140,y=165)

# email ka input idhar aayega.......ye personal details mai bhi use hoga..@domi
emaillog = Entry(main_frame, font=("Noto Sans CJK SC", 20), bg="#2C323E",fg='#E3D74A', relief="solid", bd=1)
emaillog.place(x=140,y=265)

# uid/password ka input idhar aayega......@domi
password = Entry(main_frame, font=("Noto Sans CJK SC", 20), bg="#2C323E",fg='#E3D74A', relief="solid", bd=1)
password.place(x=140,y=365)

# ye buttons ka kuch to double click ka problem hai...mohit n dev...dekh lo tum...yashaavi bhava...@domi
signup = Button(main_frame, text="Sign Up", command=signupbut, font=("Arial", 19), bg="#192130", fg="#4AD0D7", relief="raised")
signup.place(x=30,y=445)

signin = Button(main_frame, text="Already a User? Log In", font=("Arial", 19), bg="#192130", fg="#4AD0D7", relief="raised",command=login)
signin.place(x=160,y=445)

back_button=Button(loginwin, text="⬅", font=("Noto Sans CJK SC", 25), bg="#192130", fg="#4AD0D7",command=main).place(x=10, y=10)

loginwin.mainloop()
