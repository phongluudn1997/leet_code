def toman_to_integer_1(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
    s = s.replace('CM', 'DCCCC').replace('CD', 'CCCC')
    result = 0
    for i in s:
        result += roman_dict[i]
    return result


print(toman_to_integer_1(''))
