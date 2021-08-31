def increment_by_one(numbers_list, index=0):
    if index < len(numbers_list):
        numbers_list[index] += 1
        return increment_by_one(numbers_list, index + 1)
    else:
        return numbers_list
