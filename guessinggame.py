import random

print("Number Guessing Game")
print("See if you can guess the number in 5 chances ")

chances=0
number= random.randint(1,9)

while chances < 5:

    guess= int(input("What is Your Guess(1-9):"))
    
    if guess==number:
        print("Congratulations! You Won")
        break

    elif guess > number:
            print("Your guess was too high: Guess a number smaller than", guess)

    else:
            print("Your guess was too low: Guess a number higher than", guess)

    chances += 1

if not chances < 5:
    print("You Lost! The number was",number)