import random as r


class BatchGenerator:
    def __init__(self, list_of_sequences, batch_size, shuffle=False):
        """
        :param list_of_sequences: Список списков или numpy.array одинаковой длины
        :param batch_size: Размер батчей, на которые нужно разбить входные последовательности.
        Батчи последнего элемента генератора могут быть короче чем batch_size
        :param shuffle: Флаг, позволяющий перемешивать порядок элементов в последовательностях
        """
        self.batch_size = batch_size
        self.lst = [i[:] for i in list_of_sequences]
        self.lst_max_len = max(list(map(len, self.lst)))
        if shuffle:
            [r.shuffle(i) for i in self.lst]

    def __iter__(self):
        for i in range(0, self.lst_max_len, self.batch_size):
            yield [self.lst[j][i: i + self.batch_size] for j in range(len(self.lst))]
