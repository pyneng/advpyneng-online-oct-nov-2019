# -*- coding: utf-8 -*-
'''
Задание 7.5a

Переделать декоратор count_calls из задания 7.5.
Вместо вывода количества вызовов на стандартный поток вывода,
надо записать его в атрибут total_calls.

Пример работы декоратора:
In [10]: @count_calls
    ...: def f1():
    ...:     return False
    ...:

In [11]: @count_calls
    ...: def f2():
    ...:     return False
    ...:

In [12]: for _ in range(5):
    ...:     f1()
    ...:

In [13]: for _ in range(5):
    ...:     f2()
    ...:

In [14]: for _ in range(5):
    ...:     f1()
    ...:

In [15]: f1.total_calls
Out[15]: 10

In [16]: f2.total_calls
Out[16]: 5

'''


def f1():
    return True


def f2():
    return False


