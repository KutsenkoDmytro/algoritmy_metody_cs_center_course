'''
Задача на программирование: двоичный поиск

В первой строке даны целое число 1≤n≤10**5 и массив A[1…n] из
n различных натуральных чисел, не превышающих 10**9, в порядке возрастания, во второй — целое число
1≤k≤10**5 и k натуральных чисел b1,…,bk, не превышающих 10**9. Для каждого i от 1 до k необходимо вывести индекс
1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.
'''

def binary_search(key, lst):
    '''Возвращает индекс ключа в списке, если нет -1'''
    l, r = 0, len(lst)-1
    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == key:
            return middle + 1
        elif lst[middle] > key:
            r = middle - 1
        else:
            l = middle + 1
    return -1

lst_size, *lst = map(int, input().split())
num_keys, *keys = map(int, input().split())

print(*[binary_search(k, lst) for k in keys])

# print(b)
# lst = [1, 5, 8, 12, 13]
# print(binary_search(12,lst))
