from tkinter import *

def typewriter_animation(messages, text_ids, index=0, char_index=0):
    if index < len(messages):
        if char_index <= len(messages[index]):
            canvas.itemconfig(text_ids[index], text=messages[index][:char_index+1])
            window.after(50, typewriter_animation, messages, text_ids, index, char_index+1)
        else:
            window.after(500, typewriter_animation, messages, text_ids, index+1) 

def next_action():
    import page3

def on_enter(e):
    b1.config(bg='#b075f0')  # Change background color on hover

def on_leave(e):
    b1.config(bg='#008080')  # Change background color back on leave


window = Tk()

# same same nooo000 diffulunttttt....@domi
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.title("ResuCraft")
window.state('zoomed')

canvas_y = window.winfo_screenheight()
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg="#0F141E")
canvas.pack()

# motivation wala label....@domi
message =  "Intriguing narrative! , Let's distill it into a powerful resume. "
text_id = canvas.create_text((window.winfo_screenwidth() / 2), ((window.winfo_screenheight() / 2)-200),
                             text="", font=("Noto Sans CJK SC", 22, "bold"), fill="#b075f0", anchor="center")

# quali,strength,goal bol...label hi hai...@domi
message1 = 'Craft a compelling summary of your qualifications, strengths, and career goals. Let the world know what you are up to !!'
text_id1 = canvas.create_text((window.winfo_screenwidth() / 2), ((window.winfo_screenheight() / 2)-140),
                             text="", font=("Noto Sans CJK SC", 19, "bold"), fill="white", anchor="center")


# Create header label on canvas
header_label = canvas.create_text((window.winfo_screenwidth() / 2), 50,
                                  text="ResuCraft", font=("Arial", 40, "bold"), fill="#4AD0D7", anchor="center")

input_box = Text(window, font=("Arial", 16), width=80, height=8,bg='#2C323E',fg='#CCCCCC')  # Set an appropriate width and height
input_box.place(relx=0.5, rely=0.570, anchor=CENTER)

#@dev_g....iske func mai fetch/get databese ka kuch likh...i have linked it to the next page...@domi
b1 = Button(window, font=('Arial',20), text="Next", fg="black", bg="#008080", command=next_action,padx=10)
b1.place(relx=0.5, rely=0.8, anchor=CENTER)

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

typewriter_animation([message, message1], [text_id, text_id1])

window.mainloop()