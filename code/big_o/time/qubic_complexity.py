def find_permutations(characters_list):
    permutations = []

    for first_character in characters_list:
        for second_character in characters_list:
            for third_character in characters_list:
                permutation = first_character + second_character + third_character
                permutations.append(permutation)

    return permutations
