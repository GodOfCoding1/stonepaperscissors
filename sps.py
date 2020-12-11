from tkinter import *
from random import randint

chosen = None
selected = False


def winnerscreen(e, chosen):
    global root2
    root2 = Tk()
    comp = Label(root2, text=f"What computer chose: {e}", padx=5, pady=5)
    comp.pack()
    winner = whowon(e, chosen)
    WINNER1 = Label(root2, text=f"WHO WON: {winner}", padx=5, pady=5)
    WINNER1.pack()
    playagain = Button(root2, text="PLAY AGAIN", command=again)
    playagain.pack()
    root2.mainloop()


def rock1():
    global chosen
    global selected
    chosen = "ROCK"
    selected = True
    winnerscreen(e, chosen)


def paper1():
    global chosen
    chosen = "PAPER"
    global selected
    selected = True
    winnerscreen(e, chosen)


def sis():
    global chosen
    global selected
    selected = True
    chosen = "SCISSORS"
    winnerscreen(e, chosen)


def ai():
    list1 = ["ROCK", "PAPER", "SCISSORS"]
    i = randint(0, 2)
    return list1[i]


def whowon(e, p):
    if e == "ROCK" and p == "SCISSORS":
        return "COMPUTER WON"
    if e == "ROCK" and p == "ROCK":
        return "DRAW"

    if e == "ROCK" and p == "PAPER":
        return "YOU WON"

    if e == "PAPER" and p == "SCISSORS":
        return "YOU WON"
    if e == "PAPER" and p == "PAPER":
        return "DRAW"
    if e == "PAPER" and p == "ROCK":
        return "COMPUTER WON"
    if e == "SCISSORS" and p == "SCISSORS":
        return "DRAW"
    if e == "SCISSORS" and p == "PAPER":
        return "COMPUTER WON"
    if e == "SCISSORS" and p == "ROCK":
        return "YOU WON"


def main1st():
    global e
    global root
    root = Tk()

    label1 = Label(root, text="CHOSE ONE", padx=5, pady=5)
    label1.pack()

    rock = Button(root, text="ROCK", command=lambda:[rock1()])
    paper = Button(root, text="PAPER", command=paper1)
    scissors = Button(root, text="SCISSORS", command=sis)

    rock.pack()
    paper.pack()
    scissors.pack()
    e = ai()
    root.mainloop()


def again():
    root.destroy()
    root2.destroy()
    main1st()

main1st()