'''
Задача на программирование: число инверсий

Первая строка содержит число 1≤n≤10**5, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие
10**9. Необходимо посчитать число пар индексов
1≤i<j≤n, для которых A[i]>A[j].
(Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

Sample Input:

5
2 3 9 2 9

Sample Output:

2
'''


invers = 0  # Кол-во инверсий храним в глобальной переменной.


def merge(left, right):
    global invers

    l_left = len(left)
    l_right = len(right)

    i = j = 0
    res = []
    while i < l_left and j < l_right:
        if left[i] > right[j]:
            invers += l_left - i
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    if i == l_left:
        res.extend(right[j:])
    else:
        res.extend(left[i:])
    return res


def merge_sort(A, l):
    if l > 1:
        m = l // 2
        return merge(merge_sort(A[:m], m), merge_sort(A[m:], l - m))
    else:
        return A


# n = int(input())
# m = list(map(int, input().split()))

n = 5
m = [2, 3, 9, 2, 9]

merge_sort(m, n)
print(invers) #Возвращает кол-во инверсий массива.
