from tkinter import *
x= ""
win=Tk()
win.geometry("250x100")

def analysis():
   value=my_text_box.get("1.0","end-1c")
   file = open (value+'.txt', 'r')

my_text_box=Text(win, height=1, width=20)
my_text_box.pack()

comment= Button(win, height=1, width=10, text="submit", command=lambda: analysis())

comment.pack()




win.mainloop()
