from algo_profiler import Profiler

from count_recursive import count_recursive


profiler = Profiler()

profiler.run_time_check(
    func=count_recursive,
    kwargs={"n": 2900},
    iterations=1000
)
