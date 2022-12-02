from random import randint

i = 0

class Die:
    """Modeling a die"""
    def __init__(self):
        self.sides = 20

    def roll_die(self):
        print(randint(1, self.sides))

die = Die()
while i < 10:
    die.roll_die()
    i += 1