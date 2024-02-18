'''
Задача на программирование: покрыть отрезки точками


По данным
n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤10, задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:

3
1 3
2 5
3 6
Sample Output 1:

1
3
Sample Input 2:

4
4 7
1 3
2 5
5 6
Sample Output 2:

2
3 6
'''


'''
Алгоритм:
есть несколько дощечек разной длины (это наши отрезки n).
Нужно прибить их к полу так, чтобы если комната перевернулась они не попадали.
Вот минимальное количество гвоздей в этой задаче и точки куда они прибиты и будет решением.

'''

def get_points(lst:list):
    lst_s = sorted(lst, key=lambda x: x[-1]) # Сортировка по последнему значению кортежей.
    points = list()
    while lst_s:
        if points and (lst_s[0][0] <= points[-1] <= lst_s[0][1]):
            lst_s.pop(0)
            continue
        el = lst_s.pop(0)
        points.append(el[1])

    return points

n = int(input()) # Кол-во отрезков.
lst_n = [tuple(map(int,input().split())) for i in range(n)]

res = get_points(lst_n)
print(len(res),' '.join([str(p) for p in res]), sep='\n')