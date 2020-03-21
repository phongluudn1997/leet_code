def generate_triangle(num_row: int):
    if num_row <= 0:
        return list()
    elif num_row == 1:
        return [[1]]
    else:
        result = [[1]]
        for i in range(1, num_row):
            row = list()
            row.append(1)
            for j in range(1, i):
                row.append(result[i - 1][j] + result[i - 1][j - 1])
            row.append(1)
            result.append(row)
        return result


def generate(numRows):
    pascal = [[1] * i for i in range(1, numRows + 1)]
    print(pascal)
    for i in range(numRows):
        for j in range(1, i):
            print(pascal[i - 1][j] + pascal[i - 1][j - 1])
            pascal[i][j] = pascal[i - 1][j] + pascal[i - 1][j - 1]
    return pascal


result = generate(5)
print(result)


res = generate_triangle(5)
print(res)
