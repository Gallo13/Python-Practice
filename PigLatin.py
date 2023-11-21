def translate(text):
    text = text.lower().split()
    vowels = list("aeiou")
    pairs = ["ch", "qu", "rh", "th"]
    trips = ["sch", "squ", "thr"]
    exceptions = ["xray", "yttria"]
    result = []
    
    for letter in text:
        if letter[:3] in trips:
            result.append(letter[3:] + letter[:3] + "ay")
        elif letter[:2] in pairs:
            result.append(letter[2:] + letter[:2] + "ay" )
        elif letter[0] in vowels or letter in exceptions:
            result.append(letter + "ay")
        else:
            result.append(letter[1:] + letter[0] + "ay")
    return " ".join(result)
