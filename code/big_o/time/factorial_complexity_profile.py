from algo_profiler import Profiler

from factorial_complexity import find_permutations


def data_gen(list_length):
    items = []

    for number in range(list_length):
        # This keeps numbers in the range from 97 to 122,
        # which corresponds to characters from 'a' to 'z' in the ASCII code.
        truncated_number = ((number % 122) % 26) + 97
        character = chr(truncated_number)
        items.append(character)

    return {"items": [items]}

profiler = Profiler()

profiler.run_time_analysis(
    func=find_permutations,
    data_gen=data_gen,
    gen_min_arg=1,
    gen_max_arg=11,
    gen_steps=11,
    iterations=1,
    draw_chart=True
)
