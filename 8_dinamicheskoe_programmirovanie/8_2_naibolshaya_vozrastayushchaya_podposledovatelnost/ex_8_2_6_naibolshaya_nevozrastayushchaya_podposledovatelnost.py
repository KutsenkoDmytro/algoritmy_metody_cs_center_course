'''
Задача на программирование повышенной сложности: наибольшая невозрастающая подпоследовательность

Дано целое число 1≤n≤10**5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10**9.
Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину
k, во второй — её индексы 1≤i1<i2<…<ik≤n (таким образом,
A[i1]≥A[i2]≥…≥A[in]).

Sample Input:

5
5 3 4 4 2
Sample Output:

4
1 3 4 5

'''



# https://www.youtube.com/watch?v=KDf07mg10sY - Алгоритм нахождения найбольшей возрастающей подпоследовательности, работающий за O(nlogn)

def dis(A):
    n = len(A)
    inf = 10 ** 6  # max([abs(elem) for elem in A])
    L = [inf] + [-inf] * (n + 1)
    prev = []

    for i in range(n):  # куда поставить A[i]?
        left = 0
        right = n + 1
        while left + 1 < right:
            middle = (left + right) // 2
            if L[middle] >= A[i]:
                left = middle
            else:
                right = middle
        L[right] = A[i] # Хранение наибольших елементов для последовательности длинной i.
        prev.append([right, i, A[i]]) # Хранение значений предков.

    i = n + 1  # Индекс последнего элемента массива L
    while L[i] == -inf:
        i -= 1
    # i - длина наибольшей последовательности.
    # Формируем ответ.
    answ = []
    k = i
    j = len(prev) - 1
    while k != 0:
        if prev[j][0] == k:
            answ.insert(0,prev[j][1] + 1)
            k -= 1
        j -= 1
    return i, answ # Кортеж из длины наибольшей последовательности и массива индексов елементов.


print(dis([2, 3, 1, 2, 1, 3, 2, 1, 1, 2]))
