def check_divisions(number):
    dividers = []
    number /= 2

    while number >= 1:
        dividers.append(number)
        number /= 2

    return dividers
