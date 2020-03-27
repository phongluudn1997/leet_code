from decorators import working_time, working_count


@working_time
# @working_count
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


fibo = dict()


def fibonacci_vip(n):
    if n <= 1:
        return n
    if n in fibo:
        return fibo[n]

    fibo[n] = fibonacci_vip(n - 1) + fibonacci_vip(n - 2)
    return fibo[n]


@working_time
def fibo_bottom_up(n):
    if n < 2:
        return n
    fi_minus_2 = 0
    fi_minus_1 = 1
    for i in range(2, n + 1):
        fi = fi_minus_1 + fi_minus_2
        fi_minus_2, fi_minus_1 = fi_minus_1, fi
    return fi


def testing():
    for i in range(10):
        a = i
    return a


print(testing())


result = fibo_bottom_up(1)
print(result)
