import unittest
from modelacionNumerica.algorithms.SEL_Directos.gauss import gauss


class MyTestCase(unittest.TestCase):
    def test_gauss_empty(self):
        self.assertEqual([], gauss([]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
