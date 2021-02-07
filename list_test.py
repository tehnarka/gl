import unittest


class TestListMethods(unittest.TestCase):

    def test_len(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_empty_check(self):
        self.assertFalse([])
        self.assertTrue(not [])
        self.assertTrue(['a'])
        self.assertFalse(not ['a'])


if __name__ == '__main__':
    unittest.main()
