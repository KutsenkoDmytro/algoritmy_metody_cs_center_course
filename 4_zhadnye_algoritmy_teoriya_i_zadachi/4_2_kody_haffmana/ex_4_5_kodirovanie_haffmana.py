'''
Задача на программирование: кодирование Хаффмана


По данной непустой строке s длины не более 10**4, состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв k, встречающихся в строке, и размер получившейся закодированной строки. В следующих
k строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.

Sample Input 1:

a

Sample Output 1:

1 1
a: 0
0
Sample Input 2:

abacabad

Sample Output 2:

4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

'''


s = input()
# Формируем список уникальных елементов и их частот в порядке их расположения в исходной строке.
lst = []
for i in s:
    tp = (i, s.count(i))
    if tp not in lst:
        lst.append(tp)
print(lst)

# Создаем новый список lst_new, если елемент в списке lst всего 1, записываем его в новый список, с кодом 0.
lst_new = []
if len(lst) == 1:
    lst_new.append((lst[0][0],'0'))
else:
    while len(lst) >= 2:
        # Если елементов больше 2х необходимо отсортировать список по частотам ел.
        # После чего берем 2 с найменьшей частотой и склеиваем их вместе, бросая новый елемент опять в список lst.
        # Елементы которые склеиваются удаляются из списка lst и добавляются в список lst_new со значениями 0, 1 для левого и правого соответственно.
        lst.sort(key=lambda x: x[1])
        left = lst.pop(0)
        right = lst.pop(0)
        new_val = (left[0] + right[0], left[1] + right[1])
        lst_new.append((left[0],'0'))
        lst_new.append((right[0],'1'))
        lst.append(new_val)
print(lst_new)
print(lst)

#После етого разворачиваеи список lst_new.
lst_new = lst_new[::-1]

# Создаем словарь уникальных елементов и их кодов проходя по списке lst_new и склеивая символы для каждого елемента.
chars = {}
for i in lst[0][0]:
    char = ''
    for j in lst_new:
        if i in j[0]:
            char += j[1]
    chars[i] = char


#Выводим результаты:
res_str = ''.join([chars.get(i) for i in s])
print(len(lst[0][0]), len(res_str)) # Общее кол-во уникальных елементов и длина закодированой строки.
print(*[f'{k}: {v}' for k,v in chars.items()],sep='\n') # Елемент: сомвол.
print(res_str) # Закодированая строка.



