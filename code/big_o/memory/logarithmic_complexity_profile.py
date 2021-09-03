from algo_profiler import Profiler

from logarithmic_complexity import check_divisions


def data_gen(number):
    return {"number": number}

profiler = Profiler()

profiler.run_memory_analysis(
    func=check_divisions,
    data_gen=data_gen,
    gen_min_arg=10,
    gen_max_arg=1000000000000000000,
    gen_steps=100,
    draw_chart=True
)
