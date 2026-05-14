'''This is rock paper scissors

   Basically the game is just choosing rock, paper or scissors and the AI which is just using 
   the random.choice to get a choice from the variable option while the player chooses what they want'''

from ast import While
import random
import time
from tokenize import Triple

option = ["rock","paper","scissors"]

def AI():
    global aichoice
    aichoice = random.choice(option)

def choice():
    if humanchoice in option:
        return True

def legal():
    global humanchoice
    global aichoice
    if aichoice == "rock" and humanchoice == "paper":
        print("Human wins!")
    elif aichoice == "rock" and humanchoice == "scissors":
        print("AI wins!")
    elif aichoice == "rock" and humanchoice == "rock":
        print("Draw!")
    elif aichoice == "paper" and humanchoice == "scissors":
        print("Human wins!")
    elif aichoice == "paper" and humanchoice == "rock":
        print("AI wins!")
    elif aichoice == "paper" and humanchoice == "paper":
        print("Draw!")
    elif aichoice == "scissors" and humanchoice == "rock":
        print("Human wins!")
    elif aichoice == "scissors" and humanchoice == "paper":
        print("AI wins!")
    elif aichoice == "scissors" and humanchoice == "scissors":
        print("Draw!")
    else:
        print
while True:
    print("rizz")