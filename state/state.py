import unittest

class CombinationLock():
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination = "".join(map(str, combination))

    def reset(self):
        # todo - reset lock to LOCKED state
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        code = str(digit)
        if self.status == 'LOCKED':
            self.status = code
        elif self.status != 'OPEN':
            self.status += code
            if self.status == self.combination:
                self.status = 'OPEN'
            elif not self.combination.startswith(self.status):
                self.status = 'ERROR'


class Evaluate(unittest.TestCase):
    def test(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)


if __name__ == "__main__":
    unittest.main()