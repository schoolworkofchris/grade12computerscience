# Probelm 1 and 2
for i in range(10):
    print("*", end=" ")
print("")
for i in range(5):
    print("*", end=" ")
print("")
for i in range(20):
    print("*", end=" ")
print("\n")

# problem 3
for i in range (10):
    for i in range(10):
        print("*", end=" ")
    print("")

print("\n")

# Problem 4
for i in range (10):
    for i in range(5):
        print("*", end=" ")
    print("")

print("\n")

# Problem 5
for i in range (5):
    for i in range(20):
        print("*", end=" ")
    print("")

print("\n")

# Problem 6
for i in range (10):
    for i in range(10):
        print(i, end=" ")
    print("")

print("\n")

# Problem 7
for ii in range (10):
    for i in range(10):
        print(ii, end=" ")
    print("")

print("\n")

# Problem 8
for i in range (10):
    for i in range(i+1):
        print(i, end=" ")
    print("")

print("\n")

# Problem 8

x = 10
y = 0

for i in range(10):
    for i in range(y):
        print(" ", end=" ")
    y +=1
    for i in range(x):
        print(i, end=" ")
    x -= 1 
    print("")

print("\n")

# Problem 9

x = 1

for i in range(9):
    for i in range(9):
        if x < 10:
            print("", x, end=" ")
        else:
            print(x, end=" ")
        x+=1
    print("") 

print("\n")

# Problem 10

x = 1
y = 9
z = 1

for i in range(10):
    for i in range(y):
        print(" ", end=" ")
    y -=1
    for i in range(x):
        print(z, end=" ")
        z += 1
    z = 1
    x += 1 
    print("")

print("\n")
