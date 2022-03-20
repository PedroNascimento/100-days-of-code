import random

word_list = [
    "cadeira",
    "computador",
    "bicicleta",
    "caneta",
    "elefante"
]
chosen_words = random.choice(word_list)
guess = input("Guess a letter: ").lower()

for letter in chosen_words:
    if letter == guess:
        print("Certo!")
    else:
        print("Errado!")

print(chosen_words)

