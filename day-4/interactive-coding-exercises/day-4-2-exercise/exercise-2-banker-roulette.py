# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_names = len(names)
choice_names = random.randint(0, num_names -1)
person_pay = names[choice_names]
print(f"{person_pay} is going to buy the meal today!")

