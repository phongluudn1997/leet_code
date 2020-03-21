def is_happy(n):
    mem = set()
    while n not in mem:
        mem.add(n)
        n = sum([int(i) * int(i) for i in str(n)])
        print(n)
    return n == 1


def is_happy_2(n):
    total = sum([int(i)**2 for i in str(n)])
    if total == 1:
        return True
    return is_happy_2(total)


res = is_happy(19)
print(res)
