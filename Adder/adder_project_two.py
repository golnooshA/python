from tkinter import *
from math import *
from functools import total_ordering

root = Tk()

total = 0

width = 300
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))


field = ['First Number', 'Second Number']
rowF = Frame(root)
first_label = Label(rowF, width=15, text=field[0], anchor='w')
first_number = Entry(rowF)
rowF.pack(side=TOP, fill=X, padx=5, pady=5)
first_label.pack(side=LEFT)
first_number.pack(side=RIGHT, expand=YES, fill=X)


rowS = Frame(root)
second_label = Label(rowS, width=15, text=field[1], anchor='w')
second_number = Entry(rowS)
rowS.pack(side=TOP, fill=X, padx=5, pady=5)
second_label.pack(side=LEFT)
second_number.pack(side=RIGHT, expand=YES, fill=X)


result_label = Label(root)
result_label.pack(side = TOP, expand = True, fill = BOTH)



def totalFunction():
    global total
    total = sum(int(e.get()) for e in (first_number, second_number))
    result_label.config(text="Total result = %s" % total)


b=Button(root, text="Add", bg='#6545a4', fg='white', command=totalFunction)
b.pack(side = LEFT, expand = True, fill = BOTH)

root.mainloop()
