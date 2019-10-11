import pytest
import task_4_4
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_4_4, 'IPAddress')


def test_sequence_special_methods_created():
    ip = task_4_4.IPAddress('10.2.1.1')
    check_attr_or_method(ip, method='__ge__')
    check_attr_or_method(ip, method='__ne__')
    check_attr_or_method(ip, method='__le__')
    check_attr_or_method(ip, method='__gt__')


def test_methods():
    ip1 = task_4_4.IPAddress('10.10.1.1')
    ip2 = task_4_4.IPAddress('10.5.3.1')

    assert ip1 != ip2
    assert ip1 >= ip2
    assert ip1 > ip2
    assert not ip1 < ip2
