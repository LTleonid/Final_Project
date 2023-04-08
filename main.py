import random
from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("Game by LT_Leonid")
root.geometry('600x900')
root.resizable(1, 1)
c1r, c2r, c3r, c4r, c5r = int(0), int(0), int(0), int(0), int(0)
c1 = int(0)
c2 = int(0)
c3 = int(0)
c4 = int(0)
c5 = int(0)

lives = int(input("Сколько ходов?"))

black = './Black.png'
black = Image.open(black)
black = ImageTk.PhotoImage(black)

blue = './Blue.png'
blue = Image.open(blue)
blue = ImageTk.PhotoImage(blue)

green = './Green.png'
green = Image.open(green)
green = ImageTk.PhotoImage(green)

red = './Red.png'
red = Image.open(red)
red = ImageTk.PhotoImage(red)

yel = './Yellow.png'
yel = Image.open(yel)
yel = ImageTk.PhotoImage(yel)


def reset():
    global c1, c2, c3, c4, c5
    c1 = int(0)
    c2 = int(0)
    c3 = int(0)
    c4 = int(0)
    c5 = int(0)
    bs.config(state=['normal'])
    b1.config(image=black, state=['disabled']), \
        b2.config(image=black, state=['disabled']), \
        b3.config(image=black, state=['disabled']), \
        b4.config(image=black, state=['disabled']), \
        b5.config(image=black, state=['disabled'])
    bc.config(state=['disabled'])


def start():
    global c1r, c2r, c3r, c4r, c5r
    reset()
    bs.configure(state=['disabled'], text='Игра начата')
    c1r = random.randint(-1, 3)
    c2r = random.randint(-1, 3)
    c3r = random.randint(-1, 3)
    c4r = random.randint(-1, 3)
    c5r = random.randint(-1, 3)
    print(c1r, c2r, c3r, c4r, c5r)
    root.after(500, reset())
    bs.config(state=['disabled'])
    b1.config(state=['normal'])
    b2.config(state=['normal'])
    b3.config(state=['normal'])
    b4.config(state=['normal'])
    b5.config(state=['normal'])
    bc.config(state=['normal'])


def check():
	global lives
	if lives >= 1:
		lives -= 1
	    if c1 == c1r:
	        b1.config(state=['disabled'])
	    if c2 == c2r:
	        b2.config(state=['disabled'])
	    if c3 == c3r:
	        b3.config(state=['disabled'])
	    if c4 == c4r:
	        b4.config(state=['disabled'])
	    if c5 == c5r:
	        b5.config(state=['disabled'])
	elif lives < 1:
		gameover = Label(text="Вы не угадали последовательность проводов")
		gameover.pack(anchor ='up')
    	b5.config(state=['disabled'])
	if c1 == c1r and c2 == c2r and c3 == c3r and c4 == c4r and c5 == c5r:
        bs.config(state=['normal'], text='Начать')
        reset()
        print('Right!')


def color_change1():
    global c1
    c1 += 1
    print(c1)
    if c1 == 0:
        b1.configure(image=black)
    elif c1 == 1:
        b1.configure(image=blue)
    elif c1 == 2:
        b1.configure(image=green)
    elif c1 == 3:
        b1.configure(image=red)
    elif c1 == 4:
        c1 = -1
        b1.configure(image=yel)


def color_change2():
    global c2
    c2 += 1
    print(c2)
    if c2 == 0:
        b2.configure(image=black)
    elif c2 == 1:
        b2.configure(image=blue)
    elif c2 == 2:
        b2.configure(image=green)
    elif c2 == 3:
        b2.configure(image=red)
    elif c2 == 4:
        b2.configure(image=yel)
        c2 = -1


def color_change3():
    global c3
    c3 += 1
    print(c3)
    if c3 == 0:
        b3.configure(image=black)
    elif c3 == 1:
        b3.configure(image=blue)
    elif c3 == 2:
        b3.configure(image=green)
    elif c3 == 3:
        b3.configure(image=red)
    elif c3 == 4:
        b3.configure(image=yel)
        c3 = -1


def color_change4():
    global c4
    c4 += 1
    print(c4)
    if c4 == 0:
        b4.configure(image=black)
    elif c4 == 1:
        b4.configure(image=blue)
    elif c4 == 2:
        b4.configure(image=green)
    elif c4 == 3:
        b4.configure(image=red)
    elif c4 == 4:
        c4 = -1
        b4.configure(image=yel)


def color_change5():
    global c5
    c5 += 1a
    print(c5)
    if c5 == 0:
        b5.configure(image=black)
    elif c5 == 1:
        b5.configure(image=blue)
    elif c5 == 2:
        b5.configure(image=green)
    elif c5 == 3:
        b5.configure(image=red)
    elif c5 == 4:
        c5 = -1
        b5.configure(image=yel)


title = Label \
        (
        root,
        text='Игра - "Угадай Цвет"',
        bg="black",
        fg="white",
        font=20,

    )
title.pack()

bs = Button(root, text="Старт", command=start)
bs.pack(side='top')
b1 = Button(root, text="1", command=color_change1, image=black)
b1.pack(expand=True, padx=0.1)
b2 = Button(root, text="2", command=color_change2, image=black)
b2.pack(expand=True, padx=0.1)
b3 = Button(root, text="3", command=color_change3, image=black)
b3.pack(expand=True, padx=0.1)
b4 = Button(root, text="4", command=color_change4, image=black)
b4.pack(expand=True, padx=0.1)
b5 = Button(root, text="5", command=color_change5, image=black)
b5.pack(expand=True, padx=0.1)

bc = Button(root, text='Проверить', command=check)
bc.pack(side='bottom')

reset()
root.mainloop()
