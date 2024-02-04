"""
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens.
If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
"""
def is_valid(isbn):
    isbn = str(isbn.replace('-', ''))
    if len(isbn) != 10:
        return False
    sum = 0
    for (i, digit) in enumerate(isbn):
        if digit.isdigit():
           sum += int(digit) * (10 - i)
        elif i == 9 and digit is 'X':
            sum += 10
        else:
            return False
    return sum % 11 == 0
