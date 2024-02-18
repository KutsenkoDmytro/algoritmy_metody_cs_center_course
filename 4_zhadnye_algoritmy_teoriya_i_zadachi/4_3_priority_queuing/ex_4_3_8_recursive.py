#Решение задачи рекурсивно.

class HeapMax:
    '''Очередь с приоритетом реализована с помощью структуры данных Куча.
    Элемент с наибольшим значением имеет индекс 0.
    Parent <= Right Child AND Parent <= Left Child'''

    def __init__(self):
        self._heap = list()
        self._size = -1

    @staticmethod
    def _get_parent(i):
        return int((i - 1) / 2)

    @staticmethod
    def _get_l_child(i):
        return i * 2 + 1

    @staticmethod
    def _get_r_child(i):
        return i * 2 + 2

    def insert(self, value):
        '''Добавление нового элемента в кучу.'''
        self._heap.append(value)  # Добавляем элемент в конец массива.
        self._size += 1
        self.__sift_up(self._size)

    def extract_max(self):
        '''Извлекает максимальный элемент.'''
        max_val = self._heap.pop(0)  # Удаляем максимальный элемент массива.
        self._size -= 1
        if self._heap:
            self._heap.insert(0,
                              self._heap.pop())  # Последний элемент ставим на первое место в массиве.
            self.__sift_down(0)
        print(max_val)  # Выводит максимальный элемент.

    def __sift_up(self, i):
        '''Приватный метод для метода insert.'''
        if i <= 0:
            return
        i_par = self._get_parent(i)
        if self._heap[i] > self._heap[i_par]:
            self._heap[i], self._heap[i_par] = self._heap[i_par], self._heap[i]
            i = i_par
            self.__sift_up(i)

    def __sift_down(self, i):
        '''Приватный метод для метода insert.'''
        max_indx = i
        l = self._get_l_child(i)
        if l <= self._size and self._heap[l] > self._heap[max_indx]:
            max_indx = l
        r = self._get_r_child(i)
        if r <= self._size and self._heap[r] > self._heap[max_indx]:
            max_indx = r
        if i != max_indx:
            self._heap[i], self._heap[max_indx] = self._heap[max_indx], \
            self._heap[i]
            self.__sift_down(max_indx)


bh = HeapMax()
n = int(input())
for _ in range(n):
    inp = input()
    if inp == 'ExtractMax':
        bh.extract_max()
    else:
        m, i = inp.split()
        bh.insert(int(i))