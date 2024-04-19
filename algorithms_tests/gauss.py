import unittest

import numpy as np

from modelacionNumerica.algorithms.SEL_Directos.gaussjordansolution.gauss import gauss


class MyTestCase(unittest.TestCase):
    def test_gauss_empty(self):
        self.assertEqual([], gauss([]))  # add assertion here

    def test_gauss_a1_whithoutpivot(self):
        self.assertEqual(([[1, 2, 3], [0, 0, 0], [0, 0, 0]], [0, 1, 2]), gauss([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
        self.assertEqual(([[1, 2, 3], [1, 0, 0], [1, 0, 0]], [0, 1, 2]),
                         gauss([[1, 2, 3], [1, 2, 3], [1, 2, 3]], savemultiplicator=True))

    def test_gauss_a2_withoutpivot(self):
        self.assertEqual(([[2, 1, 9], [0, 5, 3], [0, 0, 0]], [1, 0, 2]), gauss([[0, 5, 3], [2, 1, 9], [0, 0, 0]]))
        self.assertEqual(([[2, 1, 9], [0, 5, 3], [0, 0, 0]], [1, 0, 2]),
                         gauss([[0, 5, 3], [2, 1, 9], [0, 0, 0]], savemultiplicator=True))

    def test_gauss_nomatrix(self):
        self.assertRaises(Exception, gauss, [[1, 2, 3], [1, 2, 3, 4]])
        self.assertRaises(Exception, gauss, [[1, 2, 3, 4], [1, 2, 3]])

    """def test_gauss_an_withoutpivot(self):
        rng = np.random.default_rng()
        [n] = rng.integers(low=2, high=5, size=1)
        [m] = rng.integers(low=2, high=5, size=1)
        a = list(range(n))
        b = rng.integers(low=-10, high=10, size=n).tolist()
        for i in range(len(a)):
            a[i] = rng.integers(low=-10, high=10, size=m).tolist()
            a[i].append(b[i])
            print(a[i])"""


if __name__ == '__main__':
    unittest.main()
