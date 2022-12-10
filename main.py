from tkinter import *
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import math
import operator

x= ""
win=Tk()
win.geometry("500x300")
original_dic = {'0': 0,'1': 0,'2': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0 ,'9': 0 ,'a': 0,'A': 0,'b': 0,'B': 0,'c': 0,'C': 0,'d': 0,'D': 0,'e': 0,'E': 0 ,'f': 0,'F': 0,'g': 0,'G': 0,'h': 0,'H': 0,'i': 0,'I': 0,'j': 0,'J': 0,'k': 0 ,'K': 0 ,'l': 0,'L': 0,'m': 0,'M': 0,'n': 0,'N': 0,'o': 0,'O': 0,'p': 0,'P': 0 ,'q': 0,'Q': 0,'r': 0,'R': 0,'s': 0,'S': 0,'t': 0,'T': 0,'u': 0,'U': 0,'v': 0 ,'V': 0,'w': 0,'W': 0,'x': 0,'X': 0,'y': 0,'Y': 0,'z': 0,'Z': 0}
prob_dic = {'0': 0,'1': 0,'2': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0 ,'9': 0 ,'a': 0,'A': 0,'b': 0,'B': 0,'c': 0,'C': 0,'d': 0,'D': 0,'e': 0,'E': 0 ,'f': 0,'F': 0,'g': 0,'G': 0,'h': 0,'H': 0,'i': 0,'I': 0,'j': 0,'J': 0,'k': 0 ,'K': 0 ,'l': 0,'L': 0,'m': 0,'M': 0,'n': 0,'N': 0,'o': 0,'O': 0,'p': 0,'P': 0 ,'q': 0,'Q': 0,'r': 0,'R': 0,'s': 0,'S': 0,'t': 0,'T': 0,'u': 0,'U': 0,'v': 0 ,'V': 0,'w': 0,'W': 0,'x': 0,'X': 0,'y': 0,'Y': 0,'z': 0,'Z': 0}
probabilty_mean = []
probabilty_mean2 = []
probabilty_mean3 = []
probabilty_mean4 = []


def clear():
   my_text_box.delete("1.0","end")

def word_freq(string):
    text = ''.join(e for e in string if e.isalnum())
    d = Counter(''.join(text))
    sorted_keys = sorted(dict(d).keys())
    sorted_dict = {key:dict(d)[key] for key in sorted_keys}
    return (sorted_dict)

def show_pmf():
    plt.close('all')
    names = list(original_dic.keys())
    values = list(original_dic.values())
    #print (range(len(original_dic)))
    plt.bar(range(len(original_dic)), values, tick_label=names)
    plt.title("PMF")
    plt.show()

def show_cdf():
    plt.close('all')
    names = list(prob_dic.keys())
    y=list(prob_dic.values())
    cdf=np.cumsum(y)
    print (cdf)
    plt.bar(range(len(prob_dic)),cdf,tick_label=names)
    plt.title("CDF")
    plt.show()


def analysis():


   value=my_text_box.get("1.0","end-1c")
   file = open (value+'.txt', 'r')
   fileContent=file.read()

   letters =word_freq(fileContent)
   #print (letters)
   sumLetters = sum(letters.values())

   for l in letters:
        if l in original_dic:
            original_dic[l] = letters[l]
   sumLetters = sum(original_dic.values())
   for n in original_dic:
       prob_dic[n] = original_dic[n]/sumLetters

   mean.set(calc_mean())
   var.set(calc_var())
   most_letter.set(max(original_dic.items(), key=operator.itemgetter(1))[0])
   most_letterOc.set(max(original_dic.items(), key=operator.itemgetter(1))[1])
   ske.set(calc_skewness())
   kurt.set(calc_kurt())


def calc_mean():
    counter =  0
    for i in prob_dic:
       x= counter * prob_dic[i]
       counter = counter+1
       probabilty_mean.append(x)
    mean = sum(probabilty_mean)
    return mean

def calc_var():
    counter = 0
    for j in prob_dic:
       y= pow(counter,2)*prob_dic[j]
       probabilty_mean2.append(y)
       counter = counter +1
    var = sum(probabilty_mean2) - pow(sum(probabilty_mean),2)
    return var

def calc_skewness():
    counter = 0
    for j in prob_dic:
       y= pow(counter,3)*prob_dic[j]
       probabilty_mean3.append(y)
       counter = counter +1

    dom = pow(math.sqrt(sum(probabilty_mean2) - pow(sum(probabilty_mean),2)),3)
    if (dom != 0):
        ske = (sum(probabilty_mean3) - 3*sum(probabilty_mean)*(sum(probabilty_mean2) - pow(sum(probabilty_mean),2))-pow(sum(probabilty_mean),3))/pow(math.sqrt(sum(probabilty_mean2) - pow(sum(probabilty_mean),2)),3)
        return ske
    else:
        return ("None")

def calc_kurt():
    counter = 0
    for j in prob_dic:
       y= pow(counter,4)*prob_dic[j]
       probabilty_mean4.append(y)
       counter = counter +1

    dom = pow(math.sqrt(sum(probabilty_mean2) - pow(sum(probabilty_mean),2)),4)
    if (dom != 0):
        kurt = (sum(probabilty_mean3) - 3*sum(probabilty_mean)*(sum(probabilty_mean2) - pow(sum(probabilty_mean),2))-pow(sum(probabilty_mean),3))/pow(math.sqrt(sum(probabilty_mean2) - pow(sum(probabilty_mean),2)),3)
        return kurt
    else:
        return ("None")


filename_box = Label(win, text= "Filename: ")
filename_box.place(x= 105,y=0)
my_text_box=Text(win, height=1, width=20)
my_text_box.pack()



submit= Button(win, height=1, width=10, text="submit", command=lambda: analysis())
pmf_button = Button(win, height=1, width=10, text="plot pmf", command= show_pmf)
cdf_button = Button(win, height=1, width=10, text="plot cdf", command= show_cdf)
clear= Button(win, height=1, width=10,text= "Clear", command= clear)


submit.place(x=160, y =30)
clear.place(x=250, y =30)

pmf_button.place(x=160, y =60)
cdf_button.place(x=250, y =60)


mean_box = Label(win, text= "Mean: ")
mean_box.place(x=110, y=120)
var_box = Label(win, text= "Variance: ")
var_box.place(x=250, y=120)
ske_box = Label(win, text= "Skewness: ")
ske_box.place(x=110, y=170)
kurt_box = Label(win, text= "Kurtosis: ")
kurt_box.place(x=250, y=170)

most_letter_box = Label(win, text= "Most repeated: ")
most_letter_box.place(x=110, y=230)
most_letterOc_box = Label(win, text= "Occurance: ")
most_letterOc_box.place(x=250, y=230)


mean=StringVar()
var=StringVar()
ske=StringVar()
kurt= StringVar()
most_letter= StringVar()
most_letterOc= StringVar()
mean_text=Entry(win, textvariable=mean)
var_text =Entry(win, textvariable=var)
ske_text =Entry(win, textvariable=ske)
kurt_text =Entry(win, textvariable=kurt)
letter_text =Entry(win, textvariable=most_letter)
Occ_text =Entry(win, textvariable=most_letterOc)
mean_text.place(x=110, y=150)
var_text.place(x=250, y=150)
ske_text.place(x=110, y=190)
kurt_text.place(x=250, y=190)
letter_text.place(x= 110, y = 250)
Occ_text.place(x= 250, y = 250)

win.mainloop()



############################################################
########   Made by / Omar Ayyad    #########################
############################################################
