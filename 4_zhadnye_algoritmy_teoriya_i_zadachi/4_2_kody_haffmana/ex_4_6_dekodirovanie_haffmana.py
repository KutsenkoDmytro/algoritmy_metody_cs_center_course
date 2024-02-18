'''
Задача на программирование: декодирование Хаффмана

Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и
l через пробел — количество различных букв, встречающихся в строке, и размер получившейся закодированной строки, соответственно. В следующих
k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке.
В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный размер.

В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита.
Гарантируется, что длина правильного ответа не превосходит
10**4 символов.
'''


def huffman_decode(code: str, keys: dict):
    '''Возвращает декодированую строку.'''
    decode = ''
    count = 0
    while code:
        cf = code[count] if count == 0 else code[:count + 1]
        char = keys.get(cf, False)
        if char:  # Если ключ найден, добавляем значение по ключу в результирующую строку, подрузаем исходную строку о обнуляем счетчик.
            decode += char
            code = code[count + 1:]
            count = 0
        else:
            count += 1  # Иначе увеличиваем счетчик на 1.
    return decode


num_chars, code_len = map(int, input().split())
d = {j[1]: j[0] for j in [input().split(': ') for i in range(num_chars)]}
code = input()

print(huffman_decode(code, d))
