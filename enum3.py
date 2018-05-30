class AutoDict(dict):
    def __init__(self):
        self.count = 0

    def __getitem__(self, key):
        if key.startswith('__') and key.endswith('__'):
            return super().__getitem__(key)

        self[key] = self.count
        self.count += 1


class EnumMeta(type):
    def __prepare__(*args):
        return AutoDict()


class Enum(metaclass=EnumMeta):
    """
    >>> class Fruit(Enum):
    ...     apple
    ...     berry
    ...     cherry

    >>> Fruit.apple
    0

    >>> Fruit.berry
    1

    >>> Fruit.cherry
    2
    """
