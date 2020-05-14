from tkinter import *
import time


root = Tk()
root.title('Golnoosh Clock')
root.resizable(0, 0)
width = 800
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.config(bg="#ffd3d3")


Mid = Frame(root, width=600)
Mid.pack(side=TOP, expand=1)
clock = Label(Mid, font=('Courier', 50 , 'bold'), fg="#b33636", bg="#ffd3d3")
clock.pack()

def myTimer() :
    current_time = time.localtime()
    time_string = time.strftime("%m/%d/%Y %H:%M:%S", current_time)
    clock.config(text=time_string )
    clock.after(200, myTimer)


myTimer()
root.mainloop()
