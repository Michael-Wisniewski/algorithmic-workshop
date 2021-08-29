def search(names, wanted_name):
    """Time complexity - O(n)

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

    for index, name in enumerate(names):
        if name == wanted_name:
            return index

    return False
