def recursive(string, words):
    if string == '':
        return 1
    
    ways = 0
    for word in words:
        try:
            string.index(word)
        except:
            pass
        else:
            if string.index(word) == 0 and len(word) <= len(string):
                remainder = string[len(word):]
                ways += recursive(remainder, words)

    return ways


def memoization(string, words, memo={}):

    if string in memo: return memo[string]

    if string == '': return 1

    ways = 0
    for word in words:
        try:
            string.index(word)
        except:
            pass
        else:
            if string.index(word) == 0 and len(word) <= len(string):
                remainder = string[len(word):]
                ways += memoization(remainder, words)
                
    memo[string] = ways
    return ways


print(memoization('abcdef', ['abc', 'def']))
print(memoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'f']))