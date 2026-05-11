text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
for char in text:
    if char.lower() not in vowels:
        print(char, end="")

print()