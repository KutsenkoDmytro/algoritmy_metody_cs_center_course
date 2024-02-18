'''
Задача на программирование: сортировка подсчётом
Первая строка содержит число 1≤n≤10**4, вторая — n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.

Sample Input:

5
2 3 9 2 9
Sample Output:

2 2 3 9 9
'''


def count_sort(A):
    n = len(A)
    m = max(A)
    B=[0]*(m+1) #Создается доп. масив B содержащий количетво соответствующих элементов массива A (как значения) и и индексы как элементы массива A
    for j in range(0,n):
        B[A[j]] = B[A[j]] + 1
    for i in range(1,m+1):
        B[i] = B[i] + B[i-1]

    A_ = [0]*n
    for k in range(n-1, -1, -1):
        A_[B[A[k]]-1] = A[k]
        B[A[k]] = B[A[k]]-1
    return A_


A = [1,2,3,4,5,5,3,4,2,5]

print(count_sort(A))