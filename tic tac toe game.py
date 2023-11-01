from tkinter import *
from tkinter import font
import random


win=Tk()
win.geometry("300x400")
win.config(background="black")
win.title("tic tac toe game")
win.iconbitmap("tic_game.ico")

#defining functions

def glow_img(label):
    i=random.randint(1,3)
    if(i==1):
        label.config(bg="red")
    elif(i==2):
        label.config(bg="blue")
    else:
        label.config(bg="green")
    label.after(200,glow_img,label)

def next_turn(row,column):
    global player
    if button[row][column]['text']=="" and check_winner() is False:
        if(player==players[0]):

            button[row][column]['text']=player

            if check_winner() is False:
                player=players[1]
                label_1.config(text="turn:"+player)
            elif check_winner() is True:
                label_1.config(text="won:"+player)
            elif check_winner()=='Tie':
                label_1.config(text="Tie")

        else:
            button[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label_1.config(text="turn:" + player)
            elif check_winner() is True:
                label_1.config(text="won:" + player)
            elif check_winner() == 'Tie':
                label_1.config(text="Tie!")


def check_winner():
    #checking rows
    for row in range(3):
        if button[row][0]['text']==button[row][1]['text']==button[row][2]['text']!="":
            button[row][0].config(bg="green",fg="white")
            button[row][1].config(bg="green", fg="white")
            button[row][2].config(bg="green", fg="white")
            return True
    #checking columns
    for column in range(3):
        if button[0][column]['text']==button[1][column]['text']==button[2][column]['text']!="":
            button[0][column].config(bg="green", fg="white")
            button[1][column].config(bg="green", fg="white")
            button[2][column].config(bg="green", fg="white")
            return True
    #checking diagonals
    if button[0][0]['text']==button[1][1]['text']==button[2][2]['text']!="":
        button[0][0].config(bg="green", fg="white")
        button[1][1].config(bg="green", fg="white")
        button[2][2].config(bg="green", fg="white")
        return True
    elif button[0][2]['text']==button[1][1]['text']==button[2][0]['text']!="":
        button[0][2].config(bg="green", fg="white")
        button[1][1].config(bg="green", fg="white")
        button[2][0].config(bg="green", fg="white")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                button[row][column].config(bg="red",fg="white")
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if button[row][column]["text"]!="":
                spaces-=1

    if spaces==0:
        return False
    else:
        return True

def new_game():
    global player
    player=random.choice(players)
    label_1.config(text="turn:"+player)

    for row in range(3):
        for column in range(3):
            button[row][column].config(text="", highlightbackground="white", highlightcolor="white",bg="white")






#creating stuff
title_font = font.Font(family="Helvetica", size=24, weight="bold")
Img_label=Label(win, text="Tic Tac Toe Game", font=title_font,borderwidth=10, highlightbackground="white", highlightcolor="white")
players=["X","O"]
player=random.choice(players)
button = [[None,None,None] for _ in range(3)]
label_1=Label(win,text="turn-"+player,width=13,height=3,bg="black",fg="white")
x_win=Label(win,text="x-wins=",width=14,height=3,bg="black",fg="white")
o_win=Label(win,text="o-wins",width=13,height=3,bg="black",fg="white")
button[0][0] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(0, 0))
button[0][1] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(0, 1))
button[0][2] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(0, 2))
button[1][0] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(1, 0))
button[1][1] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(1, 1))
button[1][2] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(1, 2))
button[2][0] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(2, 0))
button[2][1] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(2, 1))
button[2][2] = Button(win, text="",bg="#F0F0F0", borderwidth=10, highlightbackground="white", highlightcolor="white",width=10, height=3, command=lambda: next_turn(2, 2))

restart_button=Button(win,text="restart",font=('consolas',10),borderwidth=10, highlightbackground="white", highlightcolor="white",width=39,height=3,command=new_game)

glow_img(Img_label)

#sorting stuffs
Img_label.grid(row=0,columnspan=3)
label_1.grid(row=1,column=0)
x_win.grid(row=1,column=1)
o_win.grid(row=1,column=2)
for row in range(3):
    for column in range(3):
        button[row][column].grid(row=row+2,column=column)

restart_button.grid(row=5,columnspan=3)


win=mainloop()