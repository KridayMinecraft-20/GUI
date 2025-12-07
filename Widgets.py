from tkinter import*
from datetime import date 

root = Tk()

root.geometry("300x400")
root.title("Learning about Widgets and GUI and whatever")

lbl = Label(text="Hey There!", fg="white", bg="#072fff", height=1, width=300)

name_lbl = Label(text="Full Name?", bg="#00ffa2")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to this application! \nToday's date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height = 1, bg = "#a22e00", fg = "white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()



