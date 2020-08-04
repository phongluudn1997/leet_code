def useString(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return reversedString == string


def useArray(string):
    reversedChars = list()
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return "".join(reversedChars) == string


def useRecursive(string, left=0):
    right = len(string) - 1 - left
    return True if right <= left else string[left] == string[right] and useRecursive(string, left + 1)


def useTwoPointer(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
