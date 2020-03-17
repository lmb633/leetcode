def catalan(n):
    temp = [[1 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                temp[i][j] = temp[i - 1][j]
            else:
                temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
    print(temp)
    return temp[-1][-1]


def catalan1(n):
    temp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                temp[j] = temp[j]
            else:
                temp[j] = temp[j] + temp[j - 1]
    return temp[-1]


def catalan2(n):
    result = []
    result.append(1)
    for i in range(1, n + 1):
        temp = 0
        for j in range(i):
            j0 = i - 1 - j
            temp += result[j] * result[j0]
        result.append(temp)
    print(result)
    return result[-1]


catalan2(5)
