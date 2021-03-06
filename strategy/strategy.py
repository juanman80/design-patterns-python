from abc import ABC
import math
import cmath
import unittest



class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass

    def _discriminant(self, a, b, c):
        return b**2 - 4 * a * c


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return self._discriminant(a, b, c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        dist = self._discriminant(a, b, c)
        if dist > 0:
            return dist
        return float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(disc)
        return [(-b+root_disc)/(2*a), (-b-root_disc)/(2*a)]


class Evaluate(unittest.TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(results[0].real))
        self.assertTrue(math.isnan(results[1].real))
        self.assertTrue(math.isnan(results[0].imag))
        self.assertTrue(math.isnan(results[1].imag))


if __name__ == "__main__":
    unittest.main()