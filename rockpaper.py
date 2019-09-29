import random
import time
def winner(choice):
    time.sleep(0.5)
    compchoice=random.randint(1,3)
    if compchoice==1 :
        ccn="Rock"
    elif compchoice==2:
        ccn="Paper"
    else :
        ccn="Scissor"

    if (ccn=="Rock" and choice=="Paper" ) or (ccn=="Paper" and choice=="Scissor") or  (ccn=="Scissor" and choice=="Rock" )  :
        result=name+ " Won!"
        print(" W ")

    elif ccn==choice :
        result="Turn Drawn!"
        print(" D ")

    else :
        result=name+" Lost!"    
        print(" L ")    


    global output
    output.config(text="Computer choses " + ccn + "\n" + result)

def win_r():
    winner("Rock")
def win_p():
    winner("Paper")
def win_s():
    winner("Scissor")

print("Enter your name :")
name=input("@@@@@").upper()
import tkinter
from tkinter import Button,PhotoImage,Image
from tkinter import Label  
window = tkinter.Tk()
window.title("Rock-Paper-Scissor")   

rock=Button(window,text="Rock" ,bg="tomato" ,fg="black" ,width='22', height='2' ,font=("Arial Bold",10),command=win_r)
rock.grid(row=1,column=0)

paper=Button(window,text='Paper' ,bg="Yellow" ,fg="black" ,width='22' , height='2' ,font=('Arial Bold',10) ,command=win_p)
paper.grid(row=1,column=1)

scissor=Button(window,text="Scissor" ,bg="springgreen" , fg="Black" ,width="22" , height='2',font=('Arial Bold',10),command=win_s)
scissor.grid(row=1 , column=2)

rock_image= PhotoImage(file="/home/yash/Python/rock.png")
Label(window,image=rock_image,bg="white").grid(row=0,column=0)
 
paper_image=PhotoImage(file="/home/yash/Python/paper.png")
Label(window, image=paper_image ,bg="black").grid(row=0,column=1)

scissor_image=PhotoImage(file="/home/yash/Python/scis.png")
Label(window,image=scissor_image,bg="black").grid(row=0,column=2)

winner_image=PhotoImage(file="/home/yash/Python/winner.png")
Label(window,image=winner_image,bg="black").grid(row=0,column=3)

output = tkinter.Label(window, width=24, fg = "black", text="What's your choice?",bg="orange",height='3')
output.grid(row=1,column=3)

window.mainloop()