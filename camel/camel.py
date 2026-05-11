camel = input("camelCase: ")
print("snake_case: ", end="")
for char in camel:
    if char.isupper():
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

print()