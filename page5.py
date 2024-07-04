from tkinter import *

def typewriter_animation(messages, text_ids, index=0, char_index=0):
    if index < len(messages):
        if char_index <= len(messages[index]):
            canvas.itemconfig(text_ids[index], text=messages[index][:char_index+1])
            window.after(50, typewriter_animation, messages, text_ids, index, char_index+1)
        else:
            window.after(500, typewriter_animation, messages, text_ids, index+1) 

def next_action():
    import page6

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

canvas_y = window.winfo_screenheight()
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg="#0F141E")
canvas.pack()

# tell us about ur refrences written in fancy way...@domi
message = "Every success story has its supporting cast. Do you have references ready to join your professional narrative?"
text_id = canvas.create_text((window.winfo_screenwidth() / 2), ((window.winfo_screenheight() / 2)-200),
                             text="", font=("Noto Sans CJK SC", 20, "bold"), fill="#b075f0", anchor="center")

# same as above label..@domi
message1 = 'Share their details to add depth to your journey. (If any)'
text_id1 = canvas.create_text((window.winfo_screenwidth() / 2), ((window.winfo_screenheight() / 2)-140),
                             text="", font=("Noto Sans CJK SC", 19, "bold"), fill="white", anchor="center")

# Create header label on canvas
header_label = canvas.create_text((window.winfo_screenwidth() / 2), 50,
                                  text="ResuCraft", font=("Arial", 40, "bold"), fill="#4AD0D7", anchor="center")

# input of the above ques....@domi
input_box = Text(window, font=("Arial", 16), width=80, height=8,bg='#2C323E',fg='#CCCCCC')  
input_box.place(relx=0.5, rely=0.570, anchor=CENTER)

# button....@mohit...@devg....i have directed this page to main home page...so that we can fill personal details up next...@devg modify func acc to you for database....@domi
b1 = Button(window, font=('Arial',20), text="Next", fg="black", bg="#008080", command=next_action,padx=10)
b1.place(relx=0.5, rely=0.8, anchor=CENTER)

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

typewriter_animation([message, message1], [text_id, text_id1])

window.mainloop()
