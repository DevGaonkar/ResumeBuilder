from tkinter import *

def next_action():
    import page4

def on_enter(e):
    b1.config(bg='#b075f0')  # Change background color on hover

def on_leave(e):
    b1.config(bg='#008080')  # Change background color back on leave

window = Tk()

# is almost same on every page @domi
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.title("ResuCraft")
window.state('zoomed')
window.config(bg="#0F141E")

#faltu frame hai...par important hai..as it divides 2 blocks of input info..and looks like a gareeb design  @domi
frame1=Frame(master=window,height=470,width=10,bg='#b075f0')
frame1.place(x=750,y=180)

header=Label(window,text="ResuCraft💪",font=("Noto Sans CJK SC", 40, "bold"),fg='#b075f0',bg='#0F141E')
header.place(x=620,y=50)

# statement for asking tech stack....have broken them in 2 labels for formatting purpose @domi
label1=Label(window,text="What skills and technologies are your secret weapons in the ",font=("Noto Sans CJK SC", 18, "bold"),fg='#4AD0D7',bg='#0F141E')
label1.place(x=20,y=190)
label2=Label(window,text="digital realm?? ",font=("Noto Sans CJK SC", 18, "bold"),fg='#4AD0D7',bg='#0F141E')
label2.place(x=270,y=225)

#statement for asking projects ...same same 2 parts @domi
label3=Label(window,text="Time to unveil your digital masterpieces! What remarkable  ",font=("Noto Sans CJK SC", 18, "bold"),fg='#4AD0D7',bg='#0F141E')
label3.place(x=810,y=190)
label4=Label(window,text="projects have you brought to life? ",font=("Noto Sans CJK SC", 18, "bold"),fg='#4AD0D7',bg='#0F141E')
label4.place(x=950,y=225)

#input block for tech stack
tech_stack_input=Text(window,height=15,width=58,bg='#2C323E',fg='#E3D74A',font=("Noto Sans CJK SC", 15))
tech_stack_input.place(x=50,y=300)

#input block for projects
project_input=Text(window,height=15,width=58,bg='#2C323E',fg='#E3D74A',font=("Noto Sans CJK SC", 15))
project_input.place(x=830,y=300)

# @ devg..by this time u know what to doo... :)
b1 = Button(window, font=('Arial',20), text="Next", fg="black", bg="#008080", command=next_action,padx=10)
b1.place(x=710,y=680)

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

window.mainloop()
