from tkinter import *
from collections import Counter


x= ""
win=Tk()
win.geometry("250x100")

def word_freq(string):
    text = ''.join(e for e in string if e.isalnum())
    d = Counter(''.join(text))  # count all letters
    return (dict(d))    # return a tuple of counted words and letters


def analysis():
   value=my_text_box.get("1.0","end-1c")
   file = open (value+'.txt', 'r')
   fileContent=file.read()

   letters =word_freq(fileContent)
   sumLetters = sum(letters.values())
   for l in letters:
        print("Probability of '{}': {}".format(l,letters[l]/sumLetters))


my_text_box=Text(win, height=1, width=20)
my_text_box.pack()

comment= Button(win, height=1, width=10, text="submit", command=lambda: analysis())

comment.pack()




win.mainloop()
