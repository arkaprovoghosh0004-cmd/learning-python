import random

number = random.randint(1, 20)
while True:
    try:
        guessed_number = int(input("Enter your guess: "))
    except ValueError:
        print("Please type a number.")
        continue

    # these lines must be indented at the same level as the try,
    # not inside the except
    if guessed_number > number:
        print("Too high!")
    elif guessed_number < number:
        print("Too low!")
    else:
        print("Correct! Good job!")
        break
