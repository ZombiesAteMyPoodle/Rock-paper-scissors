import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
rps_choice = int(input())
end_game = 0
result = 0
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


if rps_choice == 0:
  print(rock)
elif rps_choice == 1:
  print(paper)
elif rps_choice == 2:
  print(scissors)
else:
  end_game = 1
  
game_images = [rock, paper, scissors]
# Paper beats rock
# Rock beats scissors
# Scissors beats paper

if end_game == 0:
  computer_choice = random.randint(0, 2)
  print("\nComputer chose.\n")
  print(game_images[computer_choice])

  if computer_choice == rps_choice:
    print("It's a tie.")
    result = 2
  else:  
    if rps_choice == 0 and computer_choice == 2:
      result = 1
    elif rps_choice == 0 and computer_choice == 1:
      result = 0  
    elif rps_choice == 1 and computer_choice == 2:
      result = 0
    elif rps_choice == 1 and computer_choice == 0:
      result = 1  
    elif rps_choice == 2 and computer_choice == 0:
      result = 0
    elif rps_choice == 2 and computer_choice == 1:
      result = 1

else:
  print("Wrong choice.")


if result == 1 and end_game == 0:
  print("You win.")
if result == 0 and end_game == 0:
  print("You lose.")
