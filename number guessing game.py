#number guessing game
import random
snum = random.randint(1,9)
tries = 0
uguess = int(input("guess the number: "))

while tries < 2:
    if uguess < snum:
        uguess = int(input('too low, try again: '))
        tries += 1
    if uguess > snum:
        uguess = int(input('too high, try again: '))
        tries += 1
    if uguess == snum:
        print('You got it!')
        break
if tries == 2:
    print("You ran out of tries! The number was", snum)