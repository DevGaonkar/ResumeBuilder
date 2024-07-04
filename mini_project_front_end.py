from tkinter import *

def create_window(title):
    window = Toplevel()
    window.geometry("700x400+20+30")
    window.title(title)
    
    # Add a button to close the window
    Button(window, text="⬅", font=("Arial", 20), command=window.destroy).place(x=10, y=10)

def click_me1():
    import page1

def click_me2():
    create_window("Personal Details")

def click_me3():
    create_window("Themes")
    
def click_me4():
    create_window("Home")

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.config(bg='#0F141E')
window.title("ResuCraft-Homepage")
window.state('zoomed')

# Title Label
Label(window, text="ResuCraft💪", font=("Noto Sans CJK SC", 40, "bold"), fg="#4AD0D7", background="#0F141E").place(x=620,y=40)

f1=Frame(window,bg='#4AD0D7',height=50,width=210)
f1.place(x=680,y=200)
b1=Button(master=f1,bg='#0F141E',fg='white',text="Build your Resume", font=("Arial", 15, "bold"),command=click_me1)
b1.place(x=6,y=4)

f2=Frame(window,bg='#4AD0D7',height=50,width=184)
f2.place(x=692,y=300)
b2=Button(master=f2,bg='#0F141E',fg='white',text="Personal Details", font=("Arial", 15, "bold"),command=click_me2)
b2.place(x=6,y=4)

f3=Frame(window,bg='#4AD0D7',height=50,width=104)
f3.place(x=727,y=400)
b3=Button(master=f3,bg='#0F141E',fg='white',text="Themes", font=("Arial", 15, "bold"),command=click_me3)
b3.place(x=5,y=4)

f4=Frame(window,bg='#4AD0D7',height=50,width=51)
f4.place(x=753,y=500)
b4=Button(master=f4,bg='#0F141E',fg='white',text="🏠", font=("Arial", 15, "bold"),command=click_me4)
b4.place(x=5,y=4)

b5=Button(window,text="⬅",font=("Arial", 20, "bold"),bg="#192130",fg="#4AD0D7",command=window.destroy)
b5.place(x=5,y=5)

window.mainloop()