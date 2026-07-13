str1 = input("Enter a string: ")

n = len(str1)

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print(str1[j], end="")
        else:
            print("*", end="")
    print()