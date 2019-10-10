# -*- coding: utf-8 -*-
'''
Задание 4.4

Создать класс OrderingMixin, который будет автоматически добавлять к объекту методы:
* __ge__ - операция >=
* __ne__ - операция !=
* __le__ - операция <=
* __gt__ - операция >


OrderingMixin предполагает, что в классе уже определены методы:
* __eq__ - операция ==
* __lt__ - операция <

Проверить работу примеси можно на примере класса IPAddress.
OrderingMixin не должен использовать переменные класса IPAddress. Для работы методов
должны использоваться только существующие методы __eq__ и __lt__.
OrderingMixin должен работать и с любым другим классом у которого
есть методы __eq__ и __lt__.
'''

import ipaddress


class IPAddress:
    def __init__(self, ip):
        self._ip = int(ipaddress.ip_address(ip))

    def __str__(self):
        return f"IPAddress: {self._ip}"

    def __repr__(self):
        return f"IPAddress('{self._ip}')"

    def __eq__(self, other):
        return self._ip == other._ip

    def __lt__(self, other):
        return self._ip < other._ip


