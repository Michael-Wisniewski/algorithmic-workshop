from algo_profiler import Profiler

from fluctuating_memory_consumption import increment_by_one


def data_gen(list_length):
    """
    >>> data_gen(3)
    {'numbers_list': [0, 1, 2]}

    >>> data_gen(7)
    {'numbers_list': [0, 1, 2, 3, 4, 5, 6]}
    """

    numbers_list = [number for number in range(list_length)]
    return {"numbers_list" : numbers_list}


profiler = Profiler()

profiler.run_time_based_memory_usage(
    func=increment_by_one,
    kwargs=data_gen(10000000),
    interval=0.0001
)
