import random

secret_number = random.randint(1, 100)

print("Game: Guess the number")
print("İ picked a number from 1 to 100")

attempt = 0

while True:
    guess=int(input("Your guess:"))

    if guess>secret_number:
        print("too high")
        attempt+=1
    elif guess<secret_number:
        print("too low")
        attempt+=1
    else:
        print("You guessed it!")
        attempt+=1
        print(f'Attempts needed {attempt}')
        break