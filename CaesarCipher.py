"""
Caesar Cipher
"""
def rotate(text, key):
    encrypted = ''
    
    for t in text:
        # Check if letter in text is upper case
        if t.isupper():
            # ord() converts a character to it's numeric representation in unicode
            t_index = ord(t) - ord('A')

            # shift characters by key
            t_shift = (t_index + key) % 26 + ord('A')

            # chr() accepts a number representing the unicode of a character and returns the actual character corresponding to the numeric code
            t_new = chr(t_shift)

            encrypted += t_new

        # Check is letter in text is lower
        elif t.islower():
            # subtract the unicode of 'a' to get index in [0-25) range]
            t_index = ord(t) - ord('a')
            
            t_shift = (t_index + key) % 26 + ord('a')

            t_new = chr(t_shift)

            encrypted += t_new

        # Checks if letter in text is a digit
        elif t.isdigit():
            # if it's a number, shift its actual value
            t_new = (int(t) + key) % 10

            # if the rotated digit is greater than 9, wrap around to 0
            if t_new > 9:
                t_new = 0

            encrypted += str(t_new)

        else:
            #if it's neither alphabetical nor a number, just leave it like that
            encrypted += t
    return encrypted
