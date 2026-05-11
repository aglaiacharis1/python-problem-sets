def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for char in text:
        if char.lower() not in vowels:
           result += char
    return result


if __name__ == "__main__":
    main()