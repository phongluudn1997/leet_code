def recursive(string, words):
    if string == '': return True

    for word in words:
        try:
            string.index(word)
        except:
            pass
        else:
            if string.index(word) == 0 and len(string) >= len(word):
                remainder = string[len(word):]
                return recursive(remainder, words)
    
    return False

def memoization(string, words, memo={}):
    if string in memo: return memo[string]
    if string == '': return True

    for word in words:
        try:
            string.index(word)
        except:
            pass
        else:
            if string.index(word) == 0 and len(string) >= len(word):
                remainder = string[len(word):]
                memo[string] = memoization(remainder, words)
                return memo[string]

    memo[string] = False
    return False


print(recursive('abcdef', ['abc', 'def']))
print(recursive('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(memoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeee']))