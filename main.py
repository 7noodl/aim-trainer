from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.geometry('500x500')
root.configure(background='black')

global c
global points

count = 0

def score():
    global points
    global count

    count = count + 1
    points['text'] = count
    
def click():    
    global c

    x = random.uniform(0,1)
    y = random.uniform(0,1)

    c.destroy()
    c = Button(root, text='◉', command=lambda:[click(), score()])
    c.place(relx=x,rely=y)

def start():
    global c
    global count
    global button

    count = 1
    points['text'] = count

    x = random.uniform(0,1)
    y = random.uniform(0,1)

    button.destroy()
    label.pack_forget()

    def redo():
        global count
        global reset
        global c
        global button

        timer['text'] = 'ready?'
        points['text'] = 0

        count = 0

        c.destroy()
        reset.destroy()

        button = Button(root, text="Start", command=start)
        button.pack()

    def countdown(number):
        timer['text'] = str(number) + '...' 
        timer.configure(foreground='lightgreen')

        if number > 0:
            if number < 4:
                timer.configure(foreground='red')

            root.after(1000, countdown, number-1)

        elif number == 0:
            global reset
            messagebox.showinfo(title='wow', message=f'you scored {count} points')
            reset = Button(root, text='reset', command=redo)
            reset.configure(background='black', foreground='white')
            reset.pack()

    countdown(10)

    c = Button(root, text='◉', command=lambda:[click(), score()])
    c.place(relx=x,rely=y)
    c.pack()

timer = Label(root, text='ready?')
timer.configure(background='black', foreground='white')
timer.pack()

points = Label(root, text=count)
points.configure(background='black', foreground='white')
points.pack()

button = Button(root, text="Start", command=start)
button.pack()

label = Label(root, bg='black', text="")
label.pack()

root.mainloop()
