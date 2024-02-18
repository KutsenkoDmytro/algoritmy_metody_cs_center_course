'''
Задача на программирование: различные слагаемые
По данному числу 1≤n≤10**9  найдите максимальное число k, для которого n можно представить как сумму
k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:

4
Sample Output 1:

2
1 3
Sample Input 2:

6
Sample Output 2:

3
1 2 3
'''


def get_max_count_terms(num):
    '''Возвращает максимальное количество слагаемых числа'''
    lst_terms = []
    total = 0
    i = 1
    while total != num:
        if total + i + (i + 1) > num:
            lst_terms.append(num - total)
            break
        lst_terms.append(i)
        total += i
        i += 1
    return lst_terms

res = get_max_count_terms(int(input()))
print(len(res),' '.join([str(t) for t in res]), sep='\n')


#Мой наивный алгоритм
# def get_max_count_terms(num):
#     '''Возвращает максимальное количество слагаемых числа.'''
#     lst_terms = []
#     i = 1
#     while num:
#         b = sum(lst_terms) + i
#         if b == num:
#             lst_terms.append(i)
#             break
#         elif b + (i + 1) > num:
#             i += 1
#             continue
#         lst_terms.append(i)
#         i += 1
#     return lst_terms
#
# res = get_max_count_terms(int(input()))
# print(len(res),' '.join([str(t) for t in res]), sep='\n')