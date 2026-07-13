str1 = input("Enter a string: ")
result = ""
for ch in str1:
    if ch >= 'a' and ch <= 'z':
        result = result + chr(ord(ch) - 32)
    elif ch >= 'A' and ch <= 'Z':
        result = result + chr(ord(ch) + 32)
    else:
        result = result + ch
print(result)