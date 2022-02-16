# Challenge Day 2

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12% or 15%: "))
people = int(input("How many people to split the bill? "))

if tip == 10:
    amount = round((bill * 1.1) / people, 2)
    final_amount = "{:.2f}".format(amount)
    print(f"Each person shold pay: ${final_amount}")
elif tip == 12:
    amount = round((bill * 1.12) / people, 2)
    final_amount = "{:.2f}".format(amount)
    print(f"Each person shold pay: ${final_amount}")
elif tip == 15:
    amount = round((bill * 1.12) / people, 2)
    final_amount = "{:.2f}".format(amount)
    print(f"Each person shold pay: ${final_amount}")