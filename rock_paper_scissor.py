import random

while True:
    user = int(input("Enter 1 for rock | Enter 2 for  paper | Enter 3 for scissor: "))
    if user == 0:
        break
    

    computer = random.randint(1, 3)
    print(f"computer choice is: {computer}")

    if user == computer:
        print("Draw")
    elif user == 1:
        if computer == 2:
            print("Computer Won") 
        elif computer == 3:
            print("You Won")
    elif user == 2:
        if computer == 3:
            print("Computer Won") 
        elif computer == 1:
            print("You Won")
    elif user == 3:
        if computer == 1:
            print("Computer Won") 
        elif computer == 2:
            print("You Won")


