'''
Christian Moloci
September 10, 2022

Chapter 9: Functions
http://programarcadegames.com/index.php?chapter=lab_functions&lang=en
'''

import random

# Funtion that takes three paramaters and assigns them to a list which then is checked for min value and returned
def min3(num1, num2, num3):
    nums_list = [num1, num2, num3]
    return min(nums_list)

# Test code (from website)
print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))
print("\n")

def box(height_Num, width_Num):
    star = "*"
    for i in range(height_Num):
        print(width_Num * star)

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

# funtion to find index position
def find(my_list, index):
    try:
        print("found at index locations:", my_list.index(index) + 1 )
    except:
        print("not in list")

# Code to test with (from website)
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

# Rest my_list
my_list = []

# Function to create random list
def create_list(size):
    for i in range(size):
        list_int = random.randrange(1, 6)
        my_list.append(list_int)
    return my_list

my_list = create_list(5)
print(my_list)

# Fucntiom to count a list
def count_list(list_to_count, find_num):
    count = list_to_count.count(find_num)
    print(count, "amount of", find_num)

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

# Function to find the average of a number
def average_list(avg):
    dividing_number = len(avg)
    avg_sum = sum(avg)
    avg = avg_sum / dividing_number
    return avg

avg = average_list([1,2,3])
print(avg)

# Use the code with 1000 random nums
my_list = create_list(1000)
print(my_list)
count = count_list(my_list, 1)
avg = average_list(my_list)
print(avg)
