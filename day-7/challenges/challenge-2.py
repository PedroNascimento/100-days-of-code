import random

word_list = [
    "cadeira",
    "computador",
    "bicicleta",
    "caneta",
    "elefante"
]
chosen_words = random.choice(word_list)
print(f"A palavra escolhida é: {chosen_words}")
display = []
word_length = len(chosen_words)

# Verifica a quantidade de letras e imprime a mesma quantidade de "_"
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_words[position]
    if letter == guess:
        display[position] = letter
print(display)

