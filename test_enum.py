from enum3 import Enum


class Fruit(Enum):
    apple
    berry
    cherry


def test():
    assert Fruit.apple == 0
    assert Fruit.berry == 1
    assert Fruit.cherry == 2
