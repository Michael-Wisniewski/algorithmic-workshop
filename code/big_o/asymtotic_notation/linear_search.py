def search(names, wanted_name):
    """Time complexity - Θ(n)

    List contains wanted name.
    >>> names = ['Paul', 'Dennis', 'Gregory', 'Nathan', 'Scott', 'Julian', 'Miles', 'Laura']
    >>> wanted_name = 'Scott'
    >>> search(names, wanted_name)
    4
    
    List without wanted name.
    >>> names = ['Paul', 'Dennis', 'Gregory', 'Nathan']
    >>> wanted_name = 'Adam'
    >>> search(names, wanted_name)
    False
    """

    wanted_index = False

    for index, name in enumerate(names):
        if name == wanted_name:
            wanted_index = index

    return wanted_index
