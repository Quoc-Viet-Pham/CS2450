import random

print("Hi! I'm going to try to guess your age.")
name = input("What's your name? ")

while True:
    age_guess = random.randint(15, 30)
    answer = input(f"Are you {age_guess} years old? (y/n): ").strip().lower()

    if answer == 'y':
        print(f"Yes! {name} is {age_guess} years old.")
        break
    else:
        print("Rats.")
