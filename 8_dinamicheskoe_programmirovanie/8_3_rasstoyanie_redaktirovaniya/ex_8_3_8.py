'''
Задача на программирование: расстояние редактирования
Вычислите расстояние редактирования двух данных непустых строк длины не более
10**2 , содержащих строчные буквы латинского алфавита.

Sample Input 1:

ab
ab
Sample Output 1:

0
Sample Input 2:

short
ports
Sample Output 2:

3
'''



def diff(a, b):
    return 0 if a == b else 1

def edit_dist_bu(A, B):
    inf = float('inf')
    n = len(A) + 1  # Число строк.
    m = len(B) + 1  # Число столбцов.
    D = [[inf] * m for i in range(n)]

    for i in range(n):
        D[i][0] = i
    for j in range(m):
        D[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            c = diff(A[i - 1], B[j - 1])
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + c)
    return D[-1][-1]

A = 'horse'
B = 'ros'

print(edit_dist_bu(A, B))

