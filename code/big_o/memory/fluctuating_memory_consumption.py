def increment_by_one(numbers_list):
    incremented_list = []

    for number in numbers_list:
        incremented_number = number + 1
        incremented_list.append(incremented_number)

    for _ in range(len(numbers_list)):
        numbers_list.pop()

    return incremented_list
