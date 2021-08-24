from algo_profiler import Profiler

from quadratic_complexity import find_permutations


def data_gen(list_length):
    characters_list = []

    for number in range(list_length):
        # This keeps numbers in the range from 97 to 122,
        # which corresponds to characters from 'a' to 'z' in the ASCII code.
        truncated_number = ((number % 122) % 26) + 97
        character = chr(truncated_number)
        characters_list.append(character)

    return {"characters_list": characters_list}

profiler = Profiler()

profiler.run_time_analysis(
    func=find_permutations,
    data_gen=data_gen,
    gen_min_arg=10,
    gen_max_arg=1000,
    gen_steps=50,
    iterations=7,
    find_big_o=True
)
