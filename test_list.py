import unittest


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_illia_kripaka_fi_94_2(self):
        self.assertEqual(2*[1, 3, 5], [1, 3, 5, 1, 3, 5])

    def test_polina_kozarovitskaya(self):
        t = [1, 2, 3]
        t.clear()
        self.assertEqual(len(t), 0)


if __name__ == '__main__':
    unittest.main()
