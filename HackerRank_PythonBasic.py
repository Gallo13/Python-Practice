# 1. Python: Reverse Words and Swap Cases
# To reverse the words and swap the cases of a string in Python, you can use a combination of string manipulation functions

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Split the words in the string
    sent = sentence.split()
    
    # Reverse the order and join with spaces
    rev_sent = ' '.join(sent[::-1])
    
    # Swap case of each character
    swap_case = rev_sent.swapcase()
    
    return swap_case
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
