'''Алгоритм быстрой сортировки quick_3
Задача на программирование: точки и отрезки

В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно. Следующие
n строк содержат по два целых числа ai  и bi  (ai ≤bi ) — координаты концов отрезков. Последняя строка содержит
m целых чисел — координаты точек. Все координаты не превышают 10**8  по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

Sample Input:

2 3
0 5
7 10
1 6 11
Sample Output:

1 0 0
'''

#https://www.youtube.com/watch?v=EdhN_gEDfUM&t=360s - бинарный поиск крайней границы

from random import randrange

def partition(A, l, r):
    '''Возвращает 2 индекса k и j,где ...<A[k]==A[j]<...'''
    rd = randrange(l,r) # Выбрать рандомно элемент и поставить на первое место в списке.
    A[l], A[rd] = A[rd], A[l]
    x = A[l]  # Берется первый элемент масива (опорный элемент).
    j = l  # j присваиваем индекс левого елемента.

    for i in range(l + 1, r):  # Идем по куску массива.
        if A[i] <= x:  # Если опорный элемент больше либо равен значению на проходе цикла.
            j = j + 1  # j увеличиваем на 1 и меняем местами.
            A[j], A[i] = A[i], A[j]
    A[j], A[l] = A[l], A[j]
    k = j  # В промежутке от k до j находятся повторяющиеся элементы.
    while k - 1 >= l:
        if A[k] > A[k - 1]:
            break
        k -= 1
    return k, j


def quick_sort(A, l, r):
    '''Сортировка quick_3'''
    if l >= r:
        return
    n, m = partition(A, l, r)
    quick_sort(A, l, n)
    quick_sort(A, m + 1, r)


def right_bound(A, key):
    '''Возвращает правую крайнюю границу не большую значения ключа.'''
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


n, m = map(int,input().split()) # Количество отрезков и точек.
s_l = [] # Начала отрезков.
e_l = [] # Концы отрезков.
for i in range(n):
    s,e = map(int, input().split())
    s_l.append(s)
    e_l.append(e)
points = [int(i) for i in input().split()] # Точки.

quick_sort(s_l,0,n) # Сортировка масивов начал и концов.
quick_sort(e_l,0,n)

for p in points:
    print(right_bound(s_l, p) - right_bound(e_l, p-1), end=' ') # Вычисляем разность и выводим результат.
