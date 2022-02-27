import random

possible_outcomes = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(possible_outcomes)
    user_input = input("Please enter 'r' for rock 'p' for paper and 's' for scissors to play or type quit ").lower()
    if user_input.lower() == "quit":
        print("GOOD BYE! SEE YOU SOON")
        quit()

    # rock logic
    elif user_input.lower() == "r":
        user_input = "rock"
        if computer == "rock":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("DRAW! NOBODY WINS!")
        elif computer == "paper":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("YOU LOOSE! THE COMPUTER WINS!")
        elif computer == "scissors":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("YOU WON! CONGRATS!")

    # paper logic
    elif user_input.lower() == "p":
        user_input = "paper"
        if computer == "paper":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("DRAW! NOBODY WINS!")
        elif computer == "rock":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("YOU WON! CONGRATS!")
        elif computer == "scissors":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("YOU LOOSE! THE COMPUTER WINS!")

    # scissor logic
    elif user_input.lower() == "s":
        user_input = "scissors"
        if computer == "scissors":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("DRAW! NOBODY WINS!")
        elif computer == "rock":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("YOU LOOSE! THE COMPUTER WINS!")
        elif computer == "paper":
            print("Player:" + user_input)
            print("Computer:" + computer)
            print("YOU WON! CONGRATS!")









