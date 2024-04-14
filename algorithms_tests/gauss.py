import unittest
from modelacionNumerica.algorithms.SEL_Directos.gauss import gauss
from modelacionNumerica.algorithms.SEL_Directos.jordan import jordan
import numpy as np


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

    def test_gauss_an_withoutpivot(self):
        rng = np.random.default_rng()
        [n] = rng.integers(low=3, high=7, size=1)
        [m] = rng.integers(low=3, high=7, size=1)
        a = list(range(n))
        for i in range(len(a)):
            a[i] = rng.integers(low=-10, high=10, size=m).tolist()
            print(a[i])
        print()
        print("con gauss")
        agauss = gauss(a)[0]
        for i in range(len(agauss)):
            print(agauss[i])
        print()
        print("con jordan ahora")
        agaussjordan = jordan(agauss)
        for i in range(len(agaussjordan)):
            print(agaussjordan[i])


if __name__ == '__main__':
    unittest.main()
