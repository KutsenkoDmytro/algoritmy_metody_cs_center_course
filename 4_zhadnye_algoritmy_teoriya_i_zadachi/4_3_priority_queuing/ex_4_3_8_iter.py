'''
Задача на программирование: очередь с приоритетами


Первая строка входа содержит число операций
1 ≤ n ≤ 10**5. Каждая из последующих n строк задают операцию одного из следующих двух типов:
Insert x, где 0≤ x ≤10**9 — целое число;

ExtractMax.
Первая операция добавляет число

x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
Sample Input:

6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:

200
500
'''


class BinaryHeap:
    '''Очередь с приоритетом реализована с помощью структуры данных Куча.
    Элемент с наибольшим значением имеет индекс 0.
    Parent >= Right Child AND Parent >= Left Child'''

    def __init__(self, *args):
        self._heap = list()

    def _get_parent(self, indx):
        '''Получить родителя элемента с указанным индексом.'''
        return int((indx - 1)/2)

    def _get_l_child(self, indx):
        '''Получить левого потомка.'''
        return indx * 2 + 1

    def _get_r_child(self, indx):
        '''Получить правого потомка.'''
        return indx * 2 + 2

    def insert(self, value):
        '''Добавление нового элемента в кучу.'''
        self._heap.append(value)  # Добавляем элемент в конец масива.
        self.__sift_up()

    def extract_max(self):
        '''Вытягивание максимального элемента.'''
        max_val = self._heap.pop(0)  # Удаляем максимальный элемент масива.
        if self._heap:
            self._heap.insert(0,
                              self._heap.pop())  # Последний элемент ставим на первое место в масиве.
            self.__sift_down()
        print(max_val) # Выводит максимальный елемент.

    def __sift_up(self):
        '''Приватный метод для метода insert.'''
        ptr_lst = self._heap  # Наш масив.
        indx_ch = len(self._heap) - 1  # Индекс последнего элемента.
        child = ptr_lst[indx_ch]  # Последний элемент масива.
        indx_pr = self._get_parent(indx_ch)  # Индекс родителя.

        while child > ptr_lst[indx_pr]:
            ptr_lst[indx_ch], ptr_lst[indx_pr] = ptr_lst[indx_pr], child
            indx_ch = indx_pr
            indx_pr = self._get_parent(indx_ch)
        self._heap = ptr_lst

    def __sift_down(self):
        '''Приватный метод для метода extract_max.'''
        ptr_lst = self._heap
        indx_pr = 0  # Берем первый элемент массива.
        while True:
            parent = ptr_lst[indx_pr]
            indx_l_child = self._get_l_child(indx_pr)  # Получаем индексы левого и правого потомков.
            indx_r_child = self._get_r_child(indx_pr)

            # Выбираем большего потомка (если они существуют)
            if self.__check_indx(indx_l_child) and self.__check_indx(
                    indx_r_child):
                indx_big_child = indx_l_child if ptr_lst[indx_l_child] > ptr_lst[indx_r_child] else indx_r_child
            elif self.__check_indx(indx_l_child):
                indx_big_child = indx_l_child
            elif self.__check_indx(indx_r_child):
                indx_big_child = indx_r_child
            else:
                break  # Если потомков нет, выходим из цикла.

            # Если значение родителя меньше большего потомка, меняем их местами
            if parent < ptr_lst[indx_big_child]:
                ptr_lst[indx_pr], ptr_lst[indx_big_child] = ptr_lst[
                    indx_big_child], parent
                indx_pr = indx_big_child
            else:
                break  # Иначе прерываем цикл.

        self._heap = ptr_lst

    def __check_indx(self, indx):
        return 0 <= indx < len(self._heap)


bh = BinaryHeap()
n = int(input())
for _ in range(n):
    inp = input()
    if inp == 'ExtractMax':
        bh.extract_max()
    else:
        m, i = inp.split()
        bh.insert(int(i))


# bh = BinaryHeap()
# bh.insert(200)
# bh.insert(10)
# bh.extract_max()
# bh.insert(5)
# bh.insert(500)
# bh.extract_max()
# bh.insert(37)
# bh.insert(49)
# bh.insert(85)
# bh.insert(34)
# print(bh._heap)



# Вариант реализации через импорт модуля heapq:
#
# import heapq
# h = []
# for _ in range(int(input())):
#     s = input().split()
#     if s[0] == 'Insert':
#         heapq.heappush(h, int(s[1]) * (-1))
#     else:
#         print(heapq.heappop(h) * (-1))
