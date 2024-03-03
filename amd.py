class AdjacencyList:
    def __init__(self, size):
        """ Инициализация смежного представления последовательности.

        Args:
            size (int): Размер последовательности.
        """
        self.size = size
        self.adj_list = [[] for _ in range(size)]

    def add_edge(self, u, v):
        """
        Добавление ребра между вершинами u и v.

        Args:
            u (int): Номер вершины.
            v (int): Номер вершины.
        """
        self.adj_list[u].append(v)

    def remove_edge(self, u, v):
        """
        Удаление ребра между вершинами u и v.

        Args:
            u (int): Номер вершины.
            v (int): Номер вершины.
        """
        self.adj_list[u].remove(v)

    def get_neighbors(self, u):
        """
        Получение соседей вершины u.

        Args:
            u (int): Номер вершины.

        Returns:
            list: Список соседних вершин.
        """
        return self.adj_list[u]

    def __repr__(self):
        """
        Представление смежного представления последовательности в виде строки.

        Returns:
            str: Строковое представление смежного представления.
        """
        return str(self.adj_list)


class LinkedSeq:
    def __init__(self, size):
        """
        Инициализация связного представления последовательности.

        Args:
            size (int): Размер последовательности.
        """
        self.size = size
        self.seq = [None] * size

    def add_element(self, index, value):
        """
        Добавление элемента в указанную позицию.

        Args:
            index (int): Позиция для добавления элемента.
            value: Значение элемента.
        """
        self.seq[index] = value

    def remove_element(self, index):
        """
        Удаление элемента из указанной позиции.

        Args:
            index (int): Позиция для удаления элемента.
        """
        self.seq[index] = None

    def get_element(self, index):
        """
        Получение элемента по индексу.

        Args:
            index (int): Индекс элемента.

        Returns:
            object: Элемент по указанному индексу.
        """
        return self.seq[index]

    def shift_left(self, steps=1):
        """
        Сдвиг последовательности влево на указанное количество шагов.

        Args:
            steps (int): Количество шагов для сдвига (по умолчанию 1).
        """
        self.seq = self.seq[steps:] + self.seq[:steps]

    def shift_right(self, steps=1):
        """
        Сдвиг последовательности вправо на указанное количество шагов.

        Args:
            steps (int): Количество шагов для сдвига (по умолчанию 1).
        """
        self.seq = self.seq[-steps:] + self.seq[:-steps]

    def __repr__(self):
        """
        Представление связного представления последовательности в виде строки.

        Returns:
            str: Строковое представление связного представления.
        """
        return str(self.seq)


# Пример использования:

# Создание смежного представления последовательности
adj_list = AdjacencyList(5)
adj_list.add_edge(0, 1)
adj_list.add_edge(0, 2)
adj_list.add_edge(1, 3)
adj_list.add_edge(2, 4)
print("Adjacency List Representation:")
print(adj_list)

# Создание связного представления последовательности
linked_seq = LinkedSeq(5)
linked_seq.add_element(0, 'a')
linked_seq.add_element(1, 'b')
linked_seq.add_element(2, 'c')
linked_seq.add_element(3, 'd')
linked_seq.add_element(4, 'e')
print("\nLinked Sequence Representation:")
print(linked_seq)

# Добавление сдвига
print("\nShift Left:")
linked_seq.shift_left()
print(linked_seq)

print("\nShift Right:")
linked_seq.shift_right()
print(linked_seq)
