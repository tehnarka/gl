import unittest


class TestListMethods(unittest.TestCase):

    def test_polina_kozarovitskaya(self):
        t = [1, 2, 3]
        t.clear()
        self.assertEqual(len(t), 0)


if __name__ == '__main__':
    unittest.main()
