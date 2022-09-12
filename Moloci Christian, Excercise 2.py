# Christian Moloci, September 8, 2022, Excercise 2

# Vars
num = int(input("Enter an even or odd number: "))
check = float(input("Enter a number to divide by: "))

#Logic
sum_of_nums = num / check
print(sum_of_nums)

# Conditions to check if number is even or odd
if num % 4 == 0:
    print("Multiple of four")
elif num % 2 == 0:
    print("The Number is even")
else:
    print("The number is odd")

#Conditions to- check if a number is evenly divisible by another
if sum_of_nums % 2 == 0 or sum_of_nums == 1:
    print(num, "is divisible by", check)
else:
    print(num, "is not divisible by", check)

