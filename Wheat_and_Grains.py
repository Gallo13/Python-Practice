"""
Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

Write code that shows:

1) how many grains were on a given square, and
2) the total number of grains on the chessboard
"""

def square(number):
    if number >= 1 and number <= 64:
        return 1 << (number - 1)
    else:
        raise ValueError('square must be between 1 and 64')


def total():
    return (1 << 64) - 1

##############################################################

def square(number):    
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)
    
def total(number=64):
    return sum(2**(item) for item in range(number))
