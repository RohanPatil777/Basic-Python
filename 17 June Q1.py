str1 = input("Enter a string: ")

for i in range(len(str1)):

    for j in range(i):
        print("*", end="")

    print(str1[i], end="")

    for j in range(len(str1) - i - 1):
        print("*", end="")

    print()