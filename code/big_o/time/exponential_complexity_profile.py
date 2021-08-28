from algo_profiler import Profiler

from exponential_complexity import find_menu


def data_gen(list_length):
    toppings = []

    for number in range(list_length):
        # This keeps numbers in the range from 97 to 122,
        # which corresponds to characters from 'a' to 'z' in the ASCII code.
        truncated_number = ((number % 122) % 26) + 97
        character = chr(truncated_number)
        toppings.append(character)

    return {"toppings": toppings}

profiler = Profiler()

profiler.run_time_analysis(
    func=find_menu,
    data_gen=data_gen,
    gen_min_arg=1,
    gen_max_arg=27,
    gen_steps=15,
    iterations=5,
    find_big_o=True
)
