from tkinter import *
from datetime import date
baby = Tk()
baby.title('Date and something')
baby.geometry('400x300')
lbl = Label(text ='hey wassup', fg = 'black', bg = 'cyan', height = 1, width = 300)
name_lbl = Label(text = 'Siddhartha', bg ='aquamarine')
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    Message = 'hi there this is an application\n today\'s date is ' 
    greet = 'hello '+name+'\n'

    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box = Text(height = 3)
btn = Button(text = 'Begin', command = display, height = 1, bg = 'cyan', fg = 'aquamarine')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

baby.mainloop()