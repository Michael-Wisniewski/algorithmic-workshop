def check_divisions(number):
    dividers = []
    number /= 2

    while number >= 1:
        # Replaced "number" with "[number] * 10**6", because the list 
        # consisting of the integers is not enough memory to analyze results.
        dividers.append([number] * 10**6)
        number /= 2

    return dividers
