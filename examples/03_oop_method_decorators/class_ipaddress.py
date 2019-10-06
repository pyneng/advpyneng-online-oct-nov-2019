import ipaddress


## Стандартный вариант применения property без setter
class IPAddress:
    def __init__(self, ip, mask):
        print('###############__init__')
        self._ip = ip
        self._mask = mask

    @property
    def mask(self):
        print('getter')
        return self._mask

## Стандартный вариант применения property с setter
class IPAddress:
    def __init__(self, ip, mask):
        print('###############__init__')
        self._ip = ip
        self._mask = mask

    @property
    def mask(self):
        print('getter')
        return self._mask

    @mask.setter
    def mask(self, value):
        print('setter')
        if not isinstance(value, int):
            raise TypeError('Значение должно быть числом')
        if not 8 <= value <= 32:
            raise ValueError('Значение должно быть в диапазоне 8 - 32')
        self._mask = value

# Декораторы с явным setter
class IPAddress:
    def __init__(self, ip, mask):
        print('###############__init__')
        self._ip = ip
        self._mask = mask

    # создаем пустую property
    mask = property()

    # позже указываем getter
    @mask.getter
    def mask(self):
        print('getter')
        return self._mask

    @mask.setter
    def mask(self, value):
        print('setter')
        if not isinstance(value, int):
            raise TypeError('Значение должно быть числом')
        if not 8 <= value <= 32:
            raise ValueError('Значение должно быть в диапазоне 8 - 32')
        self._mask = value


# property без декораторов
class IPAddress:
    def __init__(self, ip, mask):
        print('###############__init__')
        self._ip = ip
        self._mask = mask

    def get_mask(self):
        print('getter')
        return self._mask

    def set_mask(self, value):
        print('setter')
        if not isinstance(value, int):
            raise TypeError('Значение должно быть числом')
        if not 8 <= value <= 32:
            raise ValueError('Значение должно быть в диапазоне 8 - 32')
        self._mask = value

    mask = property(get_mask, set_mask)
