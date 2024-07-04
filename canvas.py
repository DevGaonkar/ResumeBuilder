from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
from customtkinter import *

def typewriter_animation(index=0):
    global text_id
    if index < len(message):
        current_char = message[index]
        canvas.itemconfig(text_id, text=message[:index+1])
        animwin.after(75, typewriter_animation, index+1)  # Reduced delay time to 75 milliseconds
    else:
        move_canvas_up()

def move_canvas_up():
    global canvas_y, text_id

    # Move the canvas up until the text is 50 pixels from the top
    canvas_y -= 1
    canvas.move(text_id, 0, -1)
    if canvas.coords(text_id)[1] > 50:
        animwin.after(10, move_canvas_up)
    else:
        blink_exclamation()  # Call function to start blinking the exclamation mark
        create_buttons()  # Call function to create buttons once text animation is complete
        content()
        

def blink_exclamation():
    global blinking
    if not blinking:
        canvas.itemconfig(text_id, text=message.replace('!', ' '))
        blinking = True
    else:
        canvas.itemconfig(text_id, text=message)
        blinking = False
    animwin.after(500, blink_exclamation)

def create_buttons():
    # Calculate the center position of the window
    center_x = animwin.winfo_screenwidth() // 2
    center_y = animwin.winfo_screenheight() // 2

    # Create Sign Up button
    signup_button = Button(animwin, text="SignUp", font=("Noto Sans CJK SC", 22), command=signup,bg='#2C323E',fg='#4AD0D7',relief=None,bd=0)
    signup_button.place(x=890,y=560, anchor=CENTER)
    # apply_rounded_corners(signup_button, 15)

    # Create Login button
    login_button = Button(animwin, text="Login", font=("Noto Sans CJK SC", 22), command=login, bg='#2C323E',fg='#4AD0D7',relief=FLAT,bd=0,padx=20)
    login_button.place(x=640,y=560, anchor=CENTER)
    # apply_rounded_corners(login_button, 15)

def signup():
    print("Sign Up button clicked")
    import SignUp1

def login():
    print("Login button clicked")
    import login

def content():  #created by domi
    
    shirshak = Label(animwin,text="#We_beleive",font=('Noto Sans CJK SC',13,'bold'),fg='#4AD0D7',bg='#0F141E')
    shirshak1 = Label(animwin,text="#We Can,We will!",font=('Noto Sans CJK SC',13,'bold'),fg='#FFFFFF',bg='#0F141E')
    shirshak2 = Label(animwin,text="Crafting Futures, One Resume at a Time",font=('Noto Sans CJK SC',10,'bold'),fg='#4AD0D7',bg='#0F141E')
    
    k1 = Label(animwin,text="Knock Knock.....",font=('Noto Sans CJK SC',35,'bold'),fg='#FFFFFF',bg='#0F141E')
    k2 = Label(animwin,text="Did Someone Just said RESUME ???",font=('Comic Sans',43,'bold'),fg='#4AD0D7',bg='#0F141E')
    k3 = Label(animwin,text="Don't worry bro, we got your back,generate your FREE Resume Now !!",font=('Comic Sans',20,'bold'),fg='#BBC0CA',bg='#0F141E')

    shirshak.place(x=20,y=20)
    shirshak1.place(x=1360,y=20)
    shirshak2.place(x=620,y=70)
   
    k1.place(x=590,y=310)
    k2.place(x=255,y=370)
    k3.place(x=300,y=440)


global animwin
animwin = Tk()
animwin.state('zoomed')
animwin.title("Resume Builder")
animwin.geometry("1580x850")
# toplogo = PhotoImage(file='C:\\Users\\Dell\\Desktop\\mini_project_sem4\\newly_made files\\blue.png')
# animwin.iconphoto(True, toplogo)

canvas_y = animwin.winfo_screenheight()
canvas = Canvas(animwin, width=animwin.winfo_screenwidth(), height=animwin.winfo_screenheight(),bg="#0F141E")
canvas.pack()

message = "Welcome to ResuCraft.... !"
text_id = canvas.create_text((animwin.winfo_screenwidth() / 2), ((animwin.winfo_screenheight() / 2)-250),
                             text="", font=("Noto Sans CJK SC", 35, "bold"), fill="#9881A5", anchor="center")

blinking = False  # Flag to control blinking
typewriter_animation()

animwin.mainloop()
