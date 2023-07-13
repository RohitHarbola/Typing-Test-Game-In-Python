from tkinter import *
import random
import timeit
from timeit import default_timer
import difflib
import time


from datetime import datetime
from datetime import date
from tracemalloc import start

root = Tk()
##window = Tk()
root.title('PYTHON TYPING SPEED TEST')
root.geometry("1350x400")
root.resizable('false','false')
root.configure(bg="sandybrown")


entered = StringVar()
greet = Label(root, font=('arial',30,'bold'),bg="sandybrown", text="TYPING TEST")
greet.place(relx=0.5,rely=0.1,anchor=CENTER)


words = ['Let"s type type type.....and type to increase speed.','This time I will use &pici@l ch@rac@ter$.','Let us try with numbers . There are 9 apples 4 person and 2 plate','Orange','Yellow','According','Python Programming Language','Appolo Tyers','Application,with Djangoo','Blue Sky','Visulizations','MICROSOFT AZURE CLOUD services','Apple','Mango','VISUAL CODE Studio Code runner','I am devloping Python projects 0x00','This is WindoWs Os','We are Hiring so show us your skills','Lets Play a game']

word = "ARE YOU READY??"


def check():
    global entered
    global word
    global start


    string = f"{entered.get()}"
    today2=datetime.now()
    end=today2.strftime("%H:%M:%S")

    ##end = timeit.default_timer()
    FMT = "%H:%M:%S"
    s_time = datetime.strptime(end,FMT) - datetime.strptime(start,FMT)

    s_time = str(s_time)
    dif=[]
    s_time=s_time.split(":")
    for s in s_time:
        dif.append(int(s))
    time=dif[0]*3600+dif[1]*60+dif[2]

    try:
        speed = round(len(string.split()) * 60 / time, 2)
    except:
        speed=0

        if string == word:
            Msg1 = "Time= " + str(time) + 'seconds'
            Msg2 = "Accuracy= 100% "
            Msg3 = "Speed= " + str(speed) + 'wpm'


    else:
        accuracy = difflib.SequenceMatcher(None,word,string).ratio()
        accuracy = str(round(accuracy * 100, 2))
        Msg1 = "Time = " + str(time) + 'seconds'
        Msg2 = "Accuracy= " + accuracy + '%'
        Msg3 = "Speed= " + str(speed) + 'wpm' # words per minute

    label = Label(root, font=('arial', 15, 'bold'), text=Msg1)
    label.grid(row=7, columnspan=3)

    label = Label(root, font=('arial', 15, 'bold'), text=Msg2)
    label.grid(row=8, columnspan=3)

    label = Label(root, font=('arial', 15, 'bold'), text=Msg3)
    label.grid(row=9, columnspan=3)


def play():
    global word

    global entered

    today= datetime.now()
    global start
    start=today.strftime("%H:%M:%S")

    word = random.choice(words)
    label.config(text=word)
    label1 = Label(root, font=('arial', 15), text="Type here")
    label1.place(relx=0.1,rely=0.6,anchor=CENTER)

    entered = StringVar()
    enter = Entry(root, textvariable=entered, font=('arial', 15), width=80)
    enter.place(relx=0.85,rely=0.6,anchor=E)

    btn = Button(root,text="Check", command=check, bg="DodgerBlue2", fg="white", font= ('arial',10))
    btn.grid(row=6, columnspan=6)

label = Label(root, font=('arial', 20,'bold'), text=word)
label.place(relx=0.5,rely=0.4,anchor=CENTER)


s_typing = Button(root, text=" Start Typing", command=play, bg="Dodgerblue2",fg="white", font=('arial',10))
s_typing.place(relx=0.5,rely=0.23,anchor=CENTER)


mainloop() 



































































