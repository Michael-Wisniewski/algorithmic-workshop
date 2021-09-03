from algo_profiler import Profiler

from linear_complexity import init_list


def data_gen(list_length):
    return {"list_length": list_length}

profiler = Profiler()

profiler.run_memory_analysis(
    func=init_list,
    data_gen=data_gen,
    gen_min_arg=10,
    gen_max_arg=100000,
    gen_steps=100,
    find_big_o=True
)
