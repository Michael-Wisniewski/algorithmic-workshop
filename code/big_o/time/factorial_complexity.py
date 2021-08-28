from copy import deepcopy

def find_permutations(items):
    n = len(items[0])

    for i in range(n - 1):
        new_items = []

        for item in items:

            for j in range(i, n):
                new_item = deepcopy(item)
                temp = new_item[i]
                new_item[i] = new_item[j]
                new_item[j] = temp
                new_items.append(new_item)

        items = new_items

    return items
