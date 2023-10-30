#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

def play_game():
    elements = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice not in elements:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(elements)
        print(f"Computer chooses {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'scissors' and computer_choice == 'paper') or
            (player_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()

