# Christian Moloci, September 7, 2022, Excercise 3

# Vars
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_less_than_five = []
a_less_than_five_two = []
index = 0

# While loop in range 5
while a[index] <= 5:
    print(a[index])
    a_less_than_five.append(a[index])
    index += 1

# Print the new list once
print(a_less_than_five)

# Reset var
index = 0

# Inform the user of whats going on and grab input
print("Now your turn!")
range_num = int(input("What range would you like to select from: "))

# Print in range of the users request
while a[index] <= range_num:
    print(a[index])
    a_less_than_five_two.append(a[index])
    index += 1

# print the new list
print(a_less_than_five_two)