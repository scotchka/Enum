[![Build Status](https://travis-ci.org/scotchka/Enum.svg?branch=master)](https://travis-ci.org/scotchka/Enum)
[![Coverage Status](https://coveralls.io/repos/github/scotchka/Enum/badge.svg?branch=master)](https://coveralls.io/github/scotchka/Enum?branch=master)

# Enum type that autoincrements values without explicit assignment

```python
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
```

Note: requires Python 3
