'''
Задача на программирование: непрерывный рюкзак


Первая строка содержит количество предметов 1≤n≤10**3  и вместимость рюкзака 0≤W≤2⋅10**6. Каждая из следующих
n строк задаёт стоимость 0≤ci ≤2⋅10**6  и объём 0<wi ≤2⋅10**6 предмета (n,W,ci,wi  — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:

3 50
60 20
100 50
120 30
Sample Output:

180.000

'''


def fill_knapsack(weight_bp, things: list):
    lst_t = sorted(things, key=lambda x: x[0] / x[1],reverse=True)  # Сортируем по делению стоимости на объем и убыванию.
    total = 0
    while weight_bp and lst_t:  # Пока есть пространство и есть предметы которые можно взять.
        if lst_t[0][1] <= weight_bp:
            w_thing = lst_t[0][1]
            p_thing = lst_t[0][0]
        else:
            w_thing = weight_bp
            p_thing = w_thing / lst_t[0][1] * lst_t[0][0]
        total += p_thing
        weight_bp -= w_thing
        lst_t.pop(0)
    return round(float(total), 3)


n, weight_bp = map(int, input().split())  # Кол-во вещей и вес рюкзака.
lst_n = [tuple(map(int, input().split())) for i in range(n)]  # Вещи.

print(fill_knapsack(weight_bp, lst_n))
