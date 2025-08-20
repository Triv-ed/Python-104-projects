import random

print("Welcome to the Dice Game!")
user_guess = int(input("Guess a number between 1 and 6: "))
dice_roll = random.randint(1, 6)
print(f"The dice rolled: {dice_roll}")

if user_guess == dice_roll:
    print("Congratulations! You guessed it right!")
else:
    print("Sorry, better luck next time!")