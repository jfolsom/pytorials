# Guess the number
import random
secret_number = random.randint(1, 20)
print('igottanumber')

#Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is low.')
    elif guess > secret_number:
        print('Your guess is high.')
    else:
        break #If it wasn't too low or too high, it was right.

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) +
    ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))
