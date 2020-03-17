def attempt_1(n):
    result = list()
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result


def attempt_2(n):
    hash_table = {
        3: 'Fizz',
        5: 'Buzz'
    }
    result = list()
    for i in range(1, n + 1):
        string = ''
        for key in hash_table.keys():
            if i % key == 0:
                string += hash_table[key]
        if not string:
            string = str(i)
        result.append(string)
    return result


result = attempt_2(15)
print(result)
