from algo_profiler import Profiler

from logarithmic_complexity import check_divisions


def data_gen(segment):
    return {"segment": segment}

profiler = Profiler()

profiler.run_time_analysis(
    func=check_divisions,
    data_gen=data_gen,
    gen_min_arg=10,
    gen_max_arg=10000000000,
    gen_steps=100,
    iterations=10,
    find_big_o=True
)
