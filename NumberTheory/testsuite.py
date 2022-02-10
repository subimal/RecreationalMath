import unittest

class NumberTheoryTestSuite(unittest.TestCase):
        def test_GCD(self):
            from GCD import Euclid, Binary

            print("Testing GCD.Euclid and GCD.Binary")
            l = [([54, 24, 18], 6),
                    ([42, 56], 14),
                    ([461952, 116298], 18),
                    ([0, 0], 0),
                    ([0, 4], 4),
                    ([13, 0], 13)]
            for li, ansi in l:
                self.assertEqual(Euclid(li), ansi)
                self.assertEqual(Binary(li), ansi)


if __name__=='__main__':
    unittest.main()

