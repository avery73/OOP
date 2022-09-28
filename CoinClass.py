import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:     # class name ALWAYS uppercase
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):     # always use this line
        self.__sideup = 'Heads' # sideup is attribute, self is instance
                              # setting default as heads
    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self): # toss is method
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads' # __ before sideup hides attribute, it only wll print tails
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
    # program calls method, methods interact with attirubutes
    def get_sideup(self): # returns curent value of attribute
            return self.__sideup
