num = int(input("Enter a number = "))

if num < 0:
    print("Please enter a positive number")
else:
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    print(f"Reverse number = {reverse}")