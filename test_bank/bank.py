#text = input("Greeting: ").lower().strip()

#if text.startswith("hello"):
    #print("$0")
#elif text.startswith("h"):
 #   print("$20")
#else:
#    print("$100")

def main():
    answer = input("Greeting: ")
    result = value(answer)
    print(f"${result}")



def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()