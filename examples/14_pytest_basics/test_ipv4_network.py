import pytest
import class_ipv4_network
from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    '''Проверяем, что класс создан'''
    check_class_exists(class_ipv4_network, 'IPv4Network')


def test_attributes_created():
    '''
    Проверяем, что у объекта есть атрибуты:
        address, mask, broadcast, allocated
    '''
    net = class_ipv4_network.IPv4Network('100.7.1.0/26')
    check_attr_or_method(net, attr='address')
    check_attr_or_method(net, attr='mask')
    check_attr_or_method(net, attr='allocated')
    assert net.allocated == tuple(), "По умолчанию allocated должен содержать пустой кортеж"

def test_methods_created():
    '''
    Проверяем, что у объекта есть методы:
        allocate, unassigned
    '''
    net = class_ipv4_network.IPv4Network('100.7.1.0/26')
    check_attr_or_method(net, method='allocate')
    check_attr_or_method(net, method='unassigned')

def test_return_types():
    '''Проверяем работу объекта'''
    net = class_ipv4_network.IPv4Network('100.7.1.0/26')
    assert type(net.hosts()) == tuple, "Метод hosts должен возвращать кортеж"
    assert type(net.unassigned()) == tuple, "Метод unassigned должен возвращать кортеж"


def test_address_allocation():
    '''Проверяем работу объекта'''
    net = class_ipv4_network.IPv4Network('100.7.1.0/26')
    assert len(net.hosts()) == 62, "В данной сети должно быть 62 хоста"

    net.allocate('100.7.1.45')
    net.allocate('100.7.1.15')
    net.allocate('100.7.1.60')

    assert len(net.hosts()) == 62, "Метод hosts должен возвращать все хосты"
    assert len(net.allocated) == 3, "Переменная allocated должна содержать 3 хоста"
    assert len(net.unassigned()) == 59, "Метод unassigned должен возвращать на 3 хоста меньше"

