import unittest


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_polina_kozarovitskaya(self):
        l= [1,2,3]
        l.clear()
        self.assertEqual(len(l),1)
if __name__ == '__main__':
    unittest.main()
