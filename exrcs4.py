print("Odd numbers from 1 to 20: ")
for i in range(1,21):
    if(i%2 != 0):
        print(i)

print("Table of 57: ")
for i in range (1,11):
    print(57 * i)

print("Multiples of 3 except 15: ")
for i in range (1,51):
    if(i%3 == 0 and i != 15):
        print(i)

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print("Divisible by both inputs: ")
for i in range(1,1001):
    if(i%a == 0 and i%b == 0):
        print(i)
        break
