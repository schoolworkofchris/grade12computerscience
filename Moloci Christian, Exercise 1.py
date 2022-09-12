# Christian Moloci, September 7, 2022, Excercsise One

# Collect Info
age = int(input("Enter your age: "))
name = str(input("enter your Name: "))
range_num = int(input("How many times would you like to print the result: "))

# Do The Math
age_difference = 100 - age
year_of_hundred = 2022
year_of_hundred += age_difference

# Print The Results
for i in range(range_num):
    print(name, "\nWill turn 100 years old in:\n", year_of_hundred)