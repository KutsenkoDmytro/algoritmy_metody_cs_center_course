'''
Задача на программирование: калькулятор
У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом
x: заменить x на 2x, 3x или x+1. По данному целому числу 1≤n≤10**5 определите минимальное число операций
k, необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.

Sample Input 1:
1
Sample Output 1:
0
1

Sample Input 2:
5
Sample Output 2:
3
1 2 4 5

Sample Input 3:
96234
Sample Output 3:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234

'''

def calculator(n):
    inf = float('inf')
    F = [0] + ([inf] * n)
    Prev = [0] + ([inf] * n)

    for i in range(n):
        if F[i] != inf:
            for j in range(3):
                new_val = 0
                if j == 0:
                    new_val = 2 * i  # 2x
                elif j == 1:
                    new_val = 3 * i  # 3x
                elif j == 2:
                    new_val = i + 1  # x+1

                if new_val <= n and (F[new_val] > (F[i] + 1)):
                    F[new_val] = F[i] + 1
                    Prev[new_val] = i

    Ans = []
    curr = n
    while curr >= 1:
        Ans.insert(0, curr)
        curr = Prev[curr]

    return F[-1] - 1, Ans


n = 572
print(calculator(n))
