from tkinter import *

def next_action():
    pass


def on_enter(e):
    b1.config(bg='#b075f0')  # Change background color on hover

def on_leave(e):
    b1.config(bg='#008080')  # Change background color back on leave

window = Tk()
#same on almost every page.... @domi
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.state('zoomed')
window.title("ResuCraft")
window.config(bg='#0F141E')

hl = Label(window, text='ResuCraft💪', font=("Arial", 40, "bold"), fg="#4AD0D7", bg='#0F141E')
hl.place(x=620, y=20)

h1 = Label(window, text='You are almost there, just some last bits..', fg="#4AD0D7", bg='#0F141E', font=("Arial", 25, "bold"))
h1.place(x=480, y=120)

name=Label(window, text='Name :', fg="#b075f0", bg='#0F141E', font=("Arial", 25, "bold"))
name.place(x=40, y=230)
name_input=Text(window,font=("Arial", 22), width=30, height=1.2,bg='#2C323E',fg='#CCCCCC',pady=8)
name_input.place(x=160,y=230)

email=Label(window, text='Email :', fg="#b075f0", bg='#0F141E', font=("Arial", 25, "bold"))
email.place(x=830, y=230)
email_input=Text(window,font=("Arial", 22), width=30, height=1.2,bg='#2C323E',fg='#CCCCCC',pady=8)
email_input.place(x=950,y=230)

contact_num=Label(window, text='Contact Number:', fg="#b075f0", bg='#0F141E', font=("Arial", 25, "bold"))
contact_num.place(x=270, y=430)
contact_num_input=Text(window,font=("Arial", 22), width=30, height=1.2,bg='#2C323E',fg='#CCCCCC',pady=8)
contact_num_input.place(x=160,y=480)

links=Label(window, text='Github/LinkedIn Links (If any):', fg="#b075f0", bg='#0F141E', font=("Arial", 25, "bold"))
links.place(x=920, y=430)
links_input=Text(window,font=("Arial", 22), width=30, height=1.2,bg='#2C323E',fg='#CCCCCC',pady=8)
links_input.place(x=920,y=480)

b1 = Button(window, font=('Arial',20), text="Done", fg="black", bg="#b075f0", command=next_action,padx=10)
b1.place(x=710,y=600)

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

window.mainloop()