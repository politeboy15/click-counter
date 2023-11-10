from tkinter import *
from random import *
#window settings
root = Tk()
root.title("Counter of click")
root.geometry('320x400')
root.resizable(width=False, height=FALSE)
root.configure(background='yellow')

count = 0

#function for count of clicking
def clicked():
    global count
    count += 1
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    Click.configure(text=count)
#click counter settings
Click = Label(root, text="0", font='Arial 35', fg = 'green', bg='yellow')
Click.pack()
#Button settings
btn = Button(root, text="Click me!", font='Arial 35', padx='20', pady='20', command=clicked, fg = 'green')
btn.pack()

root.mainloop()