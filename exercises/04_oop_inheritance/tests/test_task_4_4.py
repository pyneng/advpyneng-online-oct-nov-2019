import pytest
import task_4_4
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_4_4, 'OrderingMixin')


def test_special_methods_created():
    class IntTest(task_4_4.OrderingMixin):
        def __init__(self, number):
            self._number = number

        def __eq__(self, other):
            return self._number == other._number

        def __lt__(self, other):
            return self._number < other._number

    int1 = IntTest(5)
    check_attr_or_method(int1, method='__ge__')
    check_attr_or_method(int1, method='__ne__')
    check_attr_or_method(int1, method='__le__')
    check_attr_or_method(int1, method='__gt__')


def test_methods():
    class IntTest(task_4_4.OrderingMixin):
        def __init__(self, number):
            self._number = number

        def __eq__(self, other):
            return self._number == other._number

        def __lt__(self, other):
            return self._number < other._number

    int1 = IntTest(5)
    int2 = IntTest(3)

    assert int1 != int2
    assert int1 >= int2
    assert int1 > int2
    assert not int1 < int2


def test_methods():
    class LettersTest(task_4_4.OrderingMixin):
        def __init__(self, letter):
            self._letter = letter

        def __eq__(self, other):
            return self._letter == other._letter

        def __lt__(self, other):
            return self._letter < other._letter

    letter1 = LettersTest('b')
    letter2 = LettersTest('a')

    assert letter1 != letter2
    assert letter1 >= letter2
    assert letter1 > letter2
    assert letter1 not < letter2
