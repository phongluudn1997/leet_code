import time


def working_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.clock()
        res = func(*args, **kwargs)
        working_time = time.clock() - t1
        print(f'Function: {func.__name__} takes {working_time}s.')
        return res
    return wrapper
