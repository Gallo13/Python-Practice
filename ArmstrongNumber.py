def is_armstrong_number(number):
    result = 0
    num_str = str(number)
    num_len = len(num_str)

    for i in num_str:
        result += int(i)**num_len
    if result > number:
        return False
    if result != number:
        return False
    return True
