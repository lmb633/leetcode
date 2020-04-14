def kmp(s, p):
    next_table = next(p)
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_table[j]
    if j == len(p) - 1:
        return True
    return False


def pmt(p):
    pmt_table = [0] * len(p)
    i = 1
    j = 0
    while i < len(p):
        if p[i] == p[j]:
            pmt_table[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pmt_table[j - 1]
    return pmt_table


def next(p):
    next_table = [0] * len(p)
    next_table[0] = -1
    i = 0
    j = -1
    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next_table[i] = j
        else:
            j = next_table[j]
    return next_table
    pass


patten = 'aaaaaaaaaaaaaaa'
print([c for c in patten])
print(pmt(patten))
print(next(patten))
