from algo_profiler import Profiler

from constant_complexity import init_list


def data_gen(digit):
    return {"digit" : digit}


profiler = Profiler()

profiler.run_memory_check(
    func=init_list,
    kwargs=data_gen(1)
)

profiler.run_memory_check(
    func=init_list,
    kwargs=data_gen(9)
)
