# Lalit is designing a game that requires simulating a dice roll. Help him implement this functionality.

import random
def roll_dice():
    return random.randint(1, 6)
print(f"You rolled a {roll_dice()}")
