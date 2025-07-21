#Console Based Rock Paper Scissors Game

import random


choices = ["rock", "paper", "scissors"]


try:
    player_1_choice = choices[int(input("Please enter \"0\" for \"rock\", enter \"1\" for \"paper\" or enter \"2\" for \"scissors\":  "))]

except:
    player_1_choice = choices[int(input("Please enter \"0\" for \"rock\", enter \"1\" for \"paper\" or enter \"2\" for \"scissors\":  "))]



computer_choice = choices[random.randint(0,2)]



print(f'You have selected: {player_1_choice}')

print(f'Computer has selected: {computer_choice}')

if player_1_choice == computer_choice:
    print("It\'s a draw")
elif (player_1_choice == "rock" and computer_choice == "scissors") or (player_1_choice == "paper" and computer_choice == "rock") or (player_1_choice == "scissors" and computer_choice == "paper"):
    print("You Win")
else:
    print("Computer Wins")