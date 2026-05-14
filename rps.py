import random 
option = ["rock", "paper", "scissors"]
cpu = random.choice(option)

def question():
 option = ["rock", "paper", "scissors"]

while True:

 decision = input(str("rock,paper,scissors? "))
 cpu = random.choice(option)


 if decision not in option:
    print("oops thats not an option please try again")
 

 else:
    print(decision)
    print(cpu)
 