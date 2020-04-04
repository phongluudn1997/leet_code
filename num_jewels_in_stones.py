def split_into_characters(string):
    result = list()
    for i in string:
        result.append(i)
    return result


class Solution:
    @classmethod
    def approach_1(cls, J, S):
        result = 0
        for i in split_into_characters(S):
            if i in J:
                result += 1
        return result

    @classmethod
    def approach_2(cls, J, S):
        result = 0
        for i in S:
            result += 1 if i in J else 0
        return result

    @classmethod
    def approach_3(cls, J, S):
        result = 0
        name = set()
        for i in S:
            print(f'Working with letter {i}')
            print(f'Set = {name}')
            print(f'Result = {result}')
            if i in name:
                print(f'{i} in set')
                result += 1
            elif i in J:
                print(f'{i} not in set, insert i into set')
                result += 1
                name.add(i)
        return result

    @classmethod
    def approach_4(cls, J, S):
        setJ = set(J)
        return sum(i in setJ for i in S)


print(Solution.approach_4('aA', 'aAAbbbb'))
