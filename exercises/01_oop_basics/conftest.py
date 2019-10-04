import pytest


def test_attr_or_method(obj, attr=None, method=None):
    if attr:
        assert getattr(obj, attr, None) != None, "Атрибут не найден"
    if method:
        assert getattr(obj, method, None) != None, "Метод не найден"

