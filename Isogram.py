def is_isogram(string):
    string = string.lower().replace(" ","").replace("-","")

    if string == '':
        return True
        
    seen_chars = set()

    for s in string:
        if s in seen_chars:
            return False
        else:
            seen_chars.add(s)

    return True
