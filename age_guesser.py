# import random

# print("Hi! I'm going to try to guess your age.")
# name = input("What's your name? ")

# while True:
#     age_guess = random.randint(15, 30)
#     answer = input(f"Are you {age_guess} years old? (y/n): ").strip().lower()

#     if answer == 'y':
#         print(f"Yes! {name} is {age_guess} years old.")
#         break
#     else:
#         print("Rats.")

import random

print("Hi! I'm going to try to guess your age.")
name = input("What's your name? ")

possible_ages = list(range(15, 31))
attempts = 0

while possible_ages:
    age_guess = random.choice(possible_ages)
    possible_ages.remove(age_guess)
    attempts += 1

    answer = input(f"Are you {age_guess} years old? (y/n): ").strip().lower()

    if answer == 'y':
        print(f"Yes! {name} is {age_guess} years old.")
        print(f"I guessed it in {attempts} tries!")
        break
    elif answer == 'n':
        print("Rats.")
    else:
        print("Please enter 'y' or 'n'.")
        possible_ages.append(age_guess)  # put it back if input was invalid

else:
    print("Hmm... I ran out of ages to guess. Are you sure you’re between 15 and 30?")
