from recviz import recviz

@recviz # Визуализация рекурсии
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)

fib1(5)



#Наивный алгоритм.
# def fib_recursive(n):
#     '''рекурсивная функция выводящая n-ое число последовательности Фибоначи'''
#     if n<=1:
#         return n
#     else:
#         return fib_recursive(n-1) + fib_recursive(n-2)
#
# print(fib_recursive(7))



def fib_table(n):
    a = 1
    b = 0
    for i in range(n):
        a, b = b, a + b
    return a
#print(fib_table(3))








