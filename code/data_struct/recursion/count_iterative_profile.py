from algo_profiler import Profiler

from count_iterative import count_iterative


profiler = Profiler()

profiler.run_time_check(
    func=count_iterative,
    kwargs={"n": 2900},
    iterations=1000
)
