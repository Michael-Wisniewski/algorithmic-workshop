from algo_profiler import Profiler

from constant_complexity import get_latst_number


def data_gen(list_length):
    numbers_list = [number for number in range(list_length)]
    return {"numbers_list": numbers_list}

profiler = Profiler()

profiler.run_time_analysis(
    func=get_latst_number,
    data_gen=data_gen,
    gen_min_arg=10,
    gen_max_arg=1000,
    gen_steps=10,
    iterations=100,
    draw_chart=True
)
