import string

def generate_alphabet_dict():
    codes = {}
    for i in range(1, 27):
        codes[string.ascii_uppercase[i-1]] = str(i)
    return codes

codes = generate_alphabet_dict()

def number_of_decode_way(string, memo={}):
    if string in memo: return memo[string]
    if string == '': return 1
    ways = 0
    for key in codes:
        try:
            string.index(codes[key])
        except:
            pass
        else:
            if string.index(codes[key]) == 0:
                remainder = string[len(codes[key]):]
                ways += number_of_decode_way(remainder)
    memo[string] = ways
    return memo[string]

print(number_of_decode_way('11106'))
print(number_of_decode_way('12'))
print(number_of_decode_way('226'))
print(number_of_decode_way('0'))