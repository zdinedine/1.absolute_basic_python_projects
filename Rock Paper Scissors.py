import random

"""Make a two-player Rock-Paper-Scissors game. (
Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock"""

Player_1 = input("Player 1 insert your name")
Player_2 = input("Player 2 insert your name")
play = "y"
while play == "y":
    Player_1_choice = input(f"{Player_1} choose ""rock"", ""paper"" or ""scissors"".")
    Player_2_choice = input(f"{Player_2} choose ""rock"", ""paper"" or ""scissors"".")
    if Player_1_choice == "rock" and Player_2_choice == "scissors":
        print(f"Congratulation {Player_1}, you won!")
        play == input("Do you want to play again?(y/n)")
    elif Player_1_choice == "rock" and Player_2_choice == "rock":
        print(f"Its draw, play again!")
        play == "y"
    elif Player_1_choice == "rock" and Player_2_choice == "paper":
        print(f"Congratulation {Player_2}, you won!")
        play == input("Do you want to play again?(y/n)")
    elif Player_1_choice == "paper" and Player_2_choice == "paper":
        print(f"Its draw, play again!")
        play == "y"
    elif Player_1_choice == "paper" and Player_2_choice == "rock":
        print(f"Congratulation {Player_1}, you won!")
        play == input("Do you want to play again?(y/n)")
    elif Player_1_choice == "paper" and Player_2_choice == "scissors":
        print(f"Congratulation {Player_2}, you won!")
        play == input("Do you want to play again?(y/n)")
    elif Player_1_choice == "scissors" and Player_2_choice == "scissors":
        print(f"Its draw, play again!")
        play == "y"
    elif Player_1_choice == "scissors" and Player_2_choice == "rock":
        print(f"Congratulation {Player_2}, you won!")
        play == input("Do you want to play again?(y/n)")
    elif Player_1_choice == "scissors" and Player_2_choice == "paper":
        print(f"Congratulation {Player_1}, you won!")
        play == input("Do you want to play again?(y/n)")
    break
