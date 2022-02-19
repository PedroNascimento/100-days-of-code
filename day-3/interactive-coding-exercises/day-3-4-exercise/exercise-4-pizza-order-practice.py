# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
bill = 0

if size == 'S':
    if add_pepperoni == "Y":
        bill = small_pizza + 2
    elif add_pepperoni == "N":
        bill = small_pizza
elif size == 'M':
    if add_pepperoni == "Y":
        bill = medium_pizza + 3
    elif add_pepperoni == "N":
        bill = medium_pizza
elif size == 'L':
    if add_pepperoni == "Y":
        bill = large_pizza + 3
    elif add_pepperoni == "N":
        bill = large_pizza

if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}")
elif extra_cheese == "N":
    print(f"Your final bill is: ${bill}")
