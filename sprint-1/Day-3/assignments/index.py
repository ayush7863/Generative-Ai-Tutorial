import random

options = ("rock", "paper", "scissors")
running = True

while running:
    user_choice = None
    computer_choice = random.choice(options)
    User = 0
    Computer = 0
    Draw = 0
    while user_choice not in options:
        user_choice = input("Enter Your Choice: ")

    print(f"Player:{user_choice}")
    print(f"Computer:{computer_choice}")

    if user_choice == computer_choice:
        Draw+=1
        print("Draw !")
    elif user_choice == "rock" and computer_choice == "scissors":
        User+=1
        print("You Win !")
    elif user_choice == "paper" and computer_choice == "rock":
        User+=1
        print("You Win !")
    elif user_choice == "scissors" and computer_choice == "paper":
        User+=1
        print("You Win!")
    else:
        Computer+=1
        print("You Lose !")
    print("Scores : User:{User}, Computer:{Computer} , Draw:{Draw}")
    play_again = input("Play again? (y/n): ").lower()


    if not play_again == "y":
        running = False


print("Thanks for playing !")
