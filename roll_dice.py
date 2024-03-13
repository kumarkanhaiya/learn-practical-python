import random

roll = random.randint(1, 6)

# print("Computer rolled " + str(roll))

guess = int(input("Guess the dice roll: "))

if roll == guess:
    print("Correct! Computer rolled a " + str(roll))
else:
    print("Wrong! Computer rolled a " + str(roll))