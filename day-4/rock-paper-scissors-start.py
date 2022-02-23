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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

choice_human = int(input("Your choice: "))
if choice_human > 2:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[choice_human])

choice_computer = random.randint(0, 2)
if choice_human <= 2:
    print(f"Computer chose: {choice_computer}")
    print(game_images[choice_computer])

if choice_human == 0 and choice_computer == 1:
    print("You lose")
elif choice_human == 0 and choice_computer == 2:
    print("You win")
elif choice_human == 1 and choice_computer == 0:
    print("You win")
elif choice_human == 1 and choice_computer == 2:
    print("You lose")
elif choice_human == 2 and choice_computer == 0:
    print("You lose")
elif choice_human == 2 and choice_computer == 1:
    print("You win")
elif choice_human == choice_computer:
    print("The match was a draw")