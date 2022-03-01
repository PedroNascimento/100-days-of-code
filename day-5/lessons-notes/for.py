# lists
# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# Function range => for loop with range

# for number in range(1, 10):
#     print(number)

count = 0
for number in range(1, 101):
    if number % 2 == 0:
        count += number
print(count)

# count = 0
# for number in range(2, 101, 2):
#     count += number
# print(count)

