from tkinter import *
from tkinter import messagebox
import random as r
#buttons=StringVar()
click=True
def button(frame):         
    b=Button(frame,padx=1,bg="white",width=3,text="   ",font=('arial',60,'bold'),bd=10)
    return b
def change_a():             
    global a
    for i in ['X','O']:
        if not(i==a):
            a=i
            break
def reset():                
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
                #PlayerX.set(0)
                #PlayerO.set(0)
    a=r.choice(['X'])
    a=r.choice(['O'])
def newgame():
    PlayerX.set(0)
    PlayerO.set(0)
    reset()

def check():                
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    n=int(PlayerO.get())
                    n1=int(PlayerX.get())
                    score=(n+1)
                    score1=(n1+1)
                    #PlayerX.set(score1)
                    #PlayerO.set(score)       
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    if a=="O":
                        PlayerO.set(score)
                    elif a=="X":
                        PlayerX.set(score1)
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        n=int(PlayerO.get())
        n1=int(PlayerX.get())
        score=(n+1)
        score1=(n1+1)
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        if a=="O":
                        PlayerO.set(score)
        elif a=="X":
                        PlayerX.set(score1)
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","It's a tie!")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
root=Tk()
PlayerX=IntVar()
PlayerO=IntVar()
PlayerX.set(0)
PlayerO.set(0)
root.title("Tic-Tac-Toe") 
RightFrame=Frame(bd=10, width=560,height=500,padx=10,pady=2,relief=RIDGE)
RightFrame.grid(row=0,column=800)
RightFrame2=Frame(bd=10, width=560,height=200,padx=10,pady=2,relief=RIDGE)
RightFrame2.grid(row=1,column=800)
RightFrame3=Frame(bd=10, width=560,height=200,padx=10,pady=2,relief=RIDGE)
RightFrame3.grid(row=2,column=800)
lblPlayerX = Label(RightFrame, font=('arial', 40, 'bold'), text="Player O: ",padx=2,pady=2)
lblPlayerX.grid(row=1,column=0)
txtPlayerX=Entry(RightFrame,font=('arial',40,'bold'),bd=2,fg="black",textvariable=PlayerX,width=14,justify=LEFT).grid(row=0,column=1)
lblPlayerO = Label(RightFrame, font=('arial', 40, 'bold'), text="Player X: ",padx=2,pady=2)
lblPlayerO.grid(row=0,column=0)
txtPlayerO=Entry(RightFrame,font=('arial',40,'bold'),bd=2,fg="black",textvariable=PlayerO,width=14,justify=LEFT).grid(row=1,column=1)
btnReset=Button(RightFrame2,text="Reset",font=('arial',40,'bold'),height=1,width=13,command=reset)
btnReset.grid(row=3,column=0,padx=6,pady=10)
btnnew=Button(RightFrame3,text="New Game",font=('arial',40,'bold'),height=1,width=13,command=newgame)
btnnew.grid(row=3,column=0,padx=6,pady=10)
a=r.choice(['X']) 
a=r.choice(['O'])           
colour={'X':"black",'O':"black"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()


