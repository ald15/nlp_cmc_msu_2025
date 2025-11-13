import random as r

class BatchGenerator:
    def f(self, list_of_sequences, batch_size: int, shuffle: bool=False):
        """
        :param list_of_sequences: Список списков или numpy.array одинаковой длины
        :param batch_size: Размер батчей, на которые нужно разбить входные последовательности.
        Батчи последнего элемента генератора могут быть короче чем batch_size
        :param shuffle: Флаг, позволяющий перемешивать порядок элементов в последовательностях
        """
        l = list_of_sequences.copy()
        [r.shuffle(l[i]) for i in range(len(l))]
        list_max_len = max(list(map(len, l)))
        for i in range(0, list_max_len - batch_size, batch_size):
            yield [l[j][i: i + batch_size]  for j in range(len(l))]

        


def main():
    t = [
            [1, 2, 3, 5, 1, 'a', 'b'], 
            [0, 0, 1, 1, 0, 1, 2]
        ]
    bg = BatchGenerator().f(
        list_of_sequences=t, 
        batch_size=2,shuffle=True
    )
    for i in bg:
        print(i)
    
    print(t)



main()