'''
Задача на программирование: рюкзак
Первая строка входа содержит целые числа
1≤W≤10**4  и 1≤n≤300 — вместимость рюкзака и число золотых слитков. Следующая строка содержит
n целых чисел 0≤w1,…,wn ≤10**5 , задающих веса слитков. Найдите максимальный вес золота, который можно унести в рюкзаке.

Sample Input:

10 3
1 4 8
Sample Output:

9

'''

# https://www.youtube.com/watch?v=S2eVYez_j58 Примеры зарач про банкомат (рюкзак с неогр. кол-вом номиналов), задачи о слитках решаемых динамическим программированием.

def knapsack_without_reps(A, S):
    '''Возвращает максимальный вес, который можно положить
    в рюкзак при ограниченом количестве элементов.
    '''
    F = [1] + ([0] * S)
    F_new = F[:]
    Prev = [-1] * (S + 1)

    for i in range(len(A)):
        for j in range(0, S + 1):
            if F[j] == 1 and (j + A[i] <= S):
                F_new[j + A[i]] = 1
                Prev[j + A[i]] = A[i]
        F = F_new
        F_new = F[:]

    print(F)
    print(Prev)
    m = len(F) - 1
    while F[m] != 1:
        m -= 1
    #return m

    # Для возвращения списка элементов.
    Ans = []
    curr = m
    while curr > 0:
        Ans.append(Prev[curr])
        curr -= Prev[curr]
    return Ans


bars = [1, 4, 8]  # Слитки.
weight_kp = 10  # Вместимость рюкзака.

print(knapsack_without_reps(bars, weight_kp))
