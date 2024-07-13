from tkinter import *
import random

# Initialize Window
root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title('Rock Paper Scissors Game BY Uttam Kumar')
root.config(bg='palegreen3')

Label(root, text='Rock - Paper - Scissors GAME', font='arial 20 bold', bg='palegreen4').pack()

# User Input for the Game
user_input = StringVar()
Label(root, text='Choose Any One : Rock🪨, Paper📄, Scissors✂️ ', font='arial 15 bold', bg='seashell').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_input, bg='springgreen3').place(x=100, y=130)

result = StringVar()

# Game Logic
def playGame():
    user_select = user_input.get()
    sys_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    if user_select == sys_choice:
        result.set(f"Tie! Both selected {sys_choice}")
    elif user_select == 'Rock':
        if sys_choice == 'Paper':
            result.set('You Lose! System selected Paper')
        else:
            result.set('You Win! System selected Scissors')
    elif user_select == 'Paper':
        if sys_choice == 'Scissors':
            result.set('You Lose! System selected Scissors')
        else:
            result.set('You Win! System selected Rock')
    elif user_select == 'Scissors':
        if sys_choice == 'Rock':
            result.set('You Lose! System selected Rock')
        else:
            result.set('You Win! System selected Paper')
    else:
        result.set("Invalid choice! Choose Rock, Paper, or Scissors")

# Reset
def Reset():
    result.set("")
    user_input.set("")

# Exit From the Game
def Exit():
    root.destroy()

# Defining Buttons and Result Entry
Entry(root, font='arial 10 bold', textvariable=result, bg='antiquewhite2', width=50).place(x=35, y=250)
Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seagreen4', command=playGame).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seagreen4', command=Reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seagreen4', command=Exit).place(x=230, y=310)

root.mainloop()
