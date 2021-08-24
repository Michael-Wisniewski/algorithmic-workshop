from algo_profiler import Profiler

from linearithmic_complexity import devide_segments


def data_gen(segment):
    segments = [segment] * segment
    return {"segments": segments}

profiler = Profiler()

profiler.run_time_analysis(
    func=devide_segments,
    data_gen=data_gen,
    gen_min_arg=10,
    gen_max_arg=100000,
    gen_steps=20,
    iterations=20,
    find_big_o=True
)
