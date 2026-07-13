num1 = int(input("num1:"))
num2 = int(input("num2:"))
smallestNum = 0

if num1 < num2:
    smallestNum = num1
else:
    smallestNum = num2

for i in range(smallestNum, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(f"HCF of {num1} and {num2} is {i}")
        break