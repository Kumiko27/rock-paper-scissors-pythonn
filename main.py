import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
# Rock 0 wins scissors 2
# Scissor 2 wins paper 1
# Paper 1 wins rock 0
game_list = [rock, paper, scissors]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if player_choose >= 3 or player_choose < 0:
    print("Invalid number")
else:
    print(game_list[player_choose])
    computer_choose = random.randint(0, 2)
    print("Computer choose:")
    print(game_list[computer_choose])
    if player_choose == computer_choose:
        print("You draw")
    elif (player_choose == 0) and (computer_choose == 2):
        print("You win!")
    elif (player_choose == 2) and (computer_choose == 1):
        print("You win!")
    elif (player_choose == 1) and (computer_choose == 0):
        print("You win!")
    else:
        print("You lose")


