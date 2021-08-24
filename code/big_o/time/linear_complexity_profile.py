from algo_profiler import Profiler

from linear_complexity import increment_by_one


def data_gen(list_length):
    numbers_list = [number for number in range(list_length)]
    return {"numbers_list": numbers_list}

profiler = Profiler()

profiler.run_time_analysis(
    func=increment_by_one,
    data_gen=data_gen,
    gen_min_arg=100,
    gen_max_arg=100000,
    gen_steps=10,
    iterations=1000,
    find_big_o=True
)
