#Пример решения с востановлением результата.
def diff(a, b):
    if a == b:
        return 0
    else:
        return 1


def edit_dist_res(a, b):
    n = len(a)
    m = len(b)
    d = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = diff(a[i - 1], b[j - 1])
            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + c)

    #Востановление результата.
    i = n
    j = m
    res = []
    while d[i][j] != 0:
        if d[i][j] == d[i - 1][j - 1] + diff(a[i - 1], b[j - 1]):
            res.append([a[i - 1], b[j - 1]])
            i -= 1
            j -= 1
        if d[i][j] == d[i - 1][j] + 1:
            res.append([a[i - 1], '-'])
            i -= 1
        if d[i][j] == d[i][j - 1] + 1:
            res.append(['-', b[j - 1]])
            j -= 1
    res.reverse()
    return res

A = 'distance'
B = 'editing'

print(edit_dist_res(A, B))