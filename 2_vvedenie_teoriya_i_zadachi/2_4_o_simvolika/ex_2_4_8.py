# Тест: правильная скорость роста
#https://www.kontrolnaya-rabota.ru/s/predel/funktsii/?function=%28x+**+2+%2F+log%28x%2C+4%29%29%2Fx+*+%28%28log%28x%2C+3%29%29+**+2%29&X=x&x0=%2Boo&side=&a0=&b0=

# from math import sqrt, log, factorial
#
# def growth_rate(coord:tuple):
#     if coord[0] == coord[1]:
#         return 'f(n) = g(n) | Верные утверждения O, Θ, Ω'
#     elif coord[0] >= coord[1]:
#         return 'f(n) >= g(n) | Верные утверждения Ω'
#     elif coord[0] <= coord[1]:
#         return 'f(n) <= g(n) | Верные утверждения O'
#
#
# f1 = lambda n: (n ** 2 / log(n, 4)) / n * ((log(n, 3)) ** 2)
# f2 = lambda n: 2 ** n / 2 ** (n + 1)
# f3 = lambda n: n**(1/2) / 5**(log(n,2))
# f4 = lambda n: 2 ** n / 2 ** (n + 1)
# f5 = lambda n: sqrt(n) / (log(n, 2)) ** 3
# f6 = lambda n: sqrt(n) / (log(n, 2)) ** 3
# f7 = lambda n: (n ** 2 / log(n, 3)) / n * ((log(n, 2)) ** 2)
#
#
# func_lst = [f1, f2, f3, f4, f5, f6, f7]
# n = 2
# n2 = 100
# f_n = [f(n) for f in func_lst]
# f_n2 = [f(n2) for f in func_lst]
# zp = list(zip(f_n, f_n2))
# print(*[growth_rate(i) for i in zp], sep='\n')


from sympy import symbols, limit, oo, log

n = symbols('n')

# Определение функций
f1 = 2 ** n
f2 = 2 ** (n + 1)

# Вычисление предела отношения функций при n стремящемся к бесконечности
relation = limit(f1 / f2, n, oo)

if relation == 0:
    print("f1 = O(f2)")
elif relation == oo:
    print("f1 = Ω(f2)")
else:
    print("f1 and f2 are in a different relationship")