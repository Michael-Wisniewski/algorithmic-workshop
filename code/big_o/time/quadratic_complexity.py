def find_permutations(characters_list):
    permutations = []

    for first_character in characters_list:
        for second_character in characters_list:
            permutations.append(first_character + second_character)

    return permutations
