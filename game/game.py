import random

while True:
    try:
        number = int(input("Level: "))
        if number > 0:
            break
    except ValueError:
        pass

target = random.randint(1, number)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
