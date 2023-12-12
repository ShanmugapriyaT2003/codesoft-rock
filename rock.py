import random
person=input("enteer the choice(rock,paper,scissors):")
computer=random.choice(person)

if person==computer:
    print("it's a tie!")
elif person=="rock":
    if computer=="scissor":
        print("computer select rock! you win!")
    else:
        print("paper cover rock ! you lose.")
elif person =="paper":
    if computer == "rock":
        print("paper covers rock! you lose.")
    else:
        print("scissors cut paper! you lose.")
elif person =="scissor":
    if computer=="paper":
        print("scissors cut paper! you win")
    else:
        print("rock smashes scissors ! you lose.")
        
