
import unittest

from abc import ABC
from collections.abc import Iterable

class Sumable(Iterable, ABC):
    @property
    def sum(self):
        ret = 0
        for s in self:
            ret += s
        return ret

class SingleValue(Sumable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

class ManyValues(list, Sumable):
    def __init__(self):
        super().__init__()

    def append(self, other):
        try:
            for o in other:
                super().append(o)
        except TypeError:
            super().append(other)


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)


if __name__ == '__main__':
    unittest.main()