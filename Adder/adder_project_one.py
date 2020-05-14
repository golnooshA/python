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


first_label = Entry(root, text="First number")
first_label.pack(side = TOP, expand = True, fill = BOTH)

second_label = Entry(root, text="Second number")
second_label.pack(side = TOP, expand = True, fill = BOTH)

result_label = Label(root)
result_label.pack(side = TOP, expand = True, fill = BOTH)


def totalFunction():
    global total
    total = sum(int(e.get()) for e in (first_label, second_label))
    result_label.config(text="Total result = %s" % total)

b=Button(root, text="Add", bg='#6545a4', fg='white', command=totalFunction)
b.pack(side = LEFT, expand = True, fill = BOTH)

root.mainloop()
