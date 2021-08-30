import random
import string

from algo_profiler import Profiler
from better_linear_search import search


def names_gen(n):
    names = []
    letters = string.ascii_lowercase

    for _ in range(n):
        random_string = "".join(
            random.choice(letters) for i in range(random.randrange(5, 10))
        )
        names.append(random_string)

    return names

def data_gen_best(n):
    wanted_name = "Alan"
    names = names_gen(n)
    names[0] = wanted_name

    return {"wanted_name": wanted_name, "names": names}


profiler = Profiler()

profiler.run_time_analysis(
    func=search,
    data_gen=data_gen_best,
    gen_min_arg=10000,
    gen_max_arg=1000000,
    gen_steps=10,
    iterations=5,
    find_big_o=True
)
