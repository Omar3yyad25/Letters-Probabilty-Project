from tkinter import *
from collections import Counter
import matplotlib.pyplot as plt

x= ""
win=Tk()
win.geometry("250x100")
original_dic = {'0': 0,'1': 0,'2': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0 ,'9': 0 ,'a': 0,'A': 0,'b': 0,'B': 0,'c': 0,'C': 0,'d': 0,'D': 0,'e': 0,'E': 0 ,'f': 0,'F': 0,'g': 0,'G': 0,'h': 0,'H': 0,'i': 0,'I': 0,'j': 0,'J': 0,'k': 0 ,'K': 0 ,'l': 0,'L': 0,'m': 0,'M': 0,'n': 0,'N': 0,'o': 0,'O': 0,'p': 0,'P': 0 ,'q': 0,'Q': 0,'r': 0,'R': 0,'s': 0,'S': 0,'t': 0,'T': 0,'u': 0,'U': 0,'v': 0 ,'V': 0,'w': 0,'W': 0,'x': 0,'X': 0,'y': 0,'Y': 0,'z': 0,'Z': 0}
probabilty_mean = []
probabilty_mean2 = []

def word_freq(string):
    text = ''.join(e for e in string if e.isalnum())
    d = Counter(''.join(text))
    sorted_keys = sorted(dict(d).keys())
    sorted_dict = {key:dict(d)[key] for key in sorted_keys}
    return (sorted_dict)

def show_pdf(dict):
     names = list(dict.keys())
     values = list(dict.values())
     plt.bar(range(len(dict)), values, tick_label=names)
     plt.show()

def analysis():

   counter =  0
   value=my_text_box.get("1.0","end-1c")
   file = open (value+'.txt', 'r')
   fileContent=file.read()

   letters =word_freq(fileContent)
   #print (letters)
   sumLetters = sum(letters.values())

   for l in letters:
        print("Probability of '{}': {}".format(l,letters[l]/sumLetters))
        if l in original_dic:
            original_dic[l] = letters[l]
   sumLetters = sum(original_dic.values())
   for n in original_dic:
       original_dic[n] = original_dic[n]/sumLetters
   print (original_dic)
   for i in original_dic:
       x= counter * original_dic[i]
       counter = counter+1
       probabilty_mean.append(x)
   counter = 0
   for j in original_dic:
       y= pow(counter,2)*original_dic[j]
       probabilty_mean2.append(y)
       counter = counter +1
   mean = sum(probabilty_mean)
   var = sum(probabilty_mean2) - pow(mean,2)
   print(mean,var)
   show_pdf(original_dic)
   show_pdf(original_dic)
   win.destroy()



my_text_box=Text(win, height=1, width=20)
my_text_box.pack()

comment= Button(win, height=1, width=10, text="submit", command=lambda: analysis())

comment.pack()




win.mainloop()
