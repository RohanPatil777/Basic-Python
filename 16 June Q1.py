num1 = int(input("num1: "))
num2 = int(input("num2: "))

if num1 > num2:
    largestNum = num1
else:
    largestNum = num2

for i in range(largestNum, num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        print(f"LCM of {num1} and {num2} is {i}")
        break