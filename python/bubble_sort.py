#!/usr/bin/env python


def bubble_sort(_array):
    x = len(_array) - 1
    count = 0
    for i in range(x):
        count += 1
        print('{}: {}'.format(count, _array))
        for j in range(x, i, -1):
            if _array[j - 1] > _array[j]:
                _array[j], _array[j - 1] = _array[j - 1], _array[j]
    return _array


if __name__ == '__main__':
    import random
    buff = [random.randint(0, 100) for i in range(10)]
    print('Data: {}'.format(buff))
    bubble_sort(buff)
    print('Result: {}'.format(buff))
