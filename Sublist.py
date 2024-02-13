"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    if list_one == [] and list_two == []:
        return EQUAL
    if list_one == [] and list_two != []:
        return SUBLIST
    if list_two == [] and list_one != []:
       return SUPERLIST
    if len(list_one) > len(list_two):
        for i in range(len(list_one)):
            if list_two == list_one[i:len(list_two)+i]:
                return SUPERLIST
    if len(list_two) > len(list_one):
        for i in range(len(list_two)):
            if list_one == list_two[i:len(list_one)+i]:
                return SUBLIST
    if list_one == list_two:
        return EQUAL
    if list_one != list_two:
        return UNEQUAL
