import pytest
import task_4_3a
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_4_3a, 'Topology')


def test_attr_topology(topology_with_dupl_links):
    '''Проверяем, что в объекте Topology есть атрибут topology'''
    top_with_data = task_4_3a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr='topology')


def test_sequence_special_methods_created():
    example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
               ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
               ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}
    top = task_4_3a.Topology(example)
    check_attr_or_method(top, method='__getitem__')
    check_attr_or_method(top, method='__setitem__')
    check_attr_or_method(top, method='__delitem__')
    check_attr_or_method(top, method='__len__')
    check_attr_or_method(top, method='__iter__')


def test_sequence_mixin_methods_created():
    example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
               ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
               ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}
    top = task_4_3a.Topology(example)
    check_attr_or_method(top, method='keys')
    check_attr_or_method(top, method='get')
    check_attr_or_method(top, method='pop')
    check_attr_or_method(top, method='clear')
    check_attr_or_method(top, method='update')


def test_methods():
    example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
               ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
               ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
               ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
               ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
               ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
    top = task_4_3a.Topology(example)
    # test __len__
    assert len(top.topology) == 3

    # test __getitem__
    assert top[('R1', 'Eth0/0')] == ('SW1', 'Eth0/1')
    assert top[('SW1', 'Eth0/1')] == ('R1', 'Eth0/0')

    # test __detitem__
    del top[('R1', 'Eth0/0')]
    assert len(top.topology) == 2

