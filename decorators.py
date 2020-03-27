import time


def working_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.clock()
        res = func(*args, **kwargs)
        working_time = time.clock() - t1
        print(f'Function: {func.__name__} takes {working_time}s.')
        return res
    return wrapper


def working_count(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'funtion {wrapper.__name__} runned {wrapper.count} times.')
        return res
    wrapper.count = 0
    return wrapper
