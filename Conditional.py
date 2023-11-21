def response(hey_bob):
    hey_bob = hey_bob.strip()

    # If there are white spaces
    if not hey_bob:
        return 'Fine. Be that way!'
    # If it contains question mark at the end
    elif hey_bob[-1] == '?':
        # If all upper case
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    # If all upper case
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
