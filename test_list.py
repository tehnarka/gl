import unittest


def get_second_to_fifth_elements(a):
    return a[2:5]


def delete_element(list1):
    list1.remove(list1[-4])
    return list1


def swap_first_last_elements(list):
    list[0], list[-1] = list[-1], list[0]
    return list


def rem_last_element(list):
    list.remove(list[-1])
    return list


def add_element(bus):
    bus = [2, 2, 0, 9, 2, 0, 0]
    bus.append(1)
    return bus


def delete(list):
    list = [3, 5, 2, 9, 8]
    list.pop()
    return list


def del_third_element(list):
    list.remove(list[-4])
    return list


class TestListMethods(unittest.TestCase):
    def test_liubov_peleshenko_fi_94(self):
        list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(swap_first_last_elements(list), [6, 2, 3, 4, 5, 1])

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_polina_kozarovitskaya(self):
        t = [1, 2, 3]
        t.clear()
        self.assertEqual(len(t), 0)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_maksym_orzhahivsky_fi_93(self):
        self.assertEqual(sum([1, 2, 3])/len([1, 2, 3]), 2)

    def test_Yegor_Panasuk_FI94(self):
        list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(rem_last_element(list), [1, 2, 3, 4, 5])

    def test_michael_medved_fi93(self):
        self.assertEqual(len([] + ['f']), len('f'))

    def test_illia_kripaka_fi_94_2(self):
        self.assertEqual(2 * [1, 3, 5], [1, 3, 5, 1, 3, 5])

    def test_maria_martynova_fi_93(self):
        self.assertEqual(len([0]), 1)
        self.assertEqual(len([1, 1]), 2)

    def test_kostiantyn_baievskyi_fi_93(self):
        self.assertEqual([1, 2, 3] + [4, 5, 6], [1, 2, 3, 4, 5, 6])

    def test_schifrin_denis_fi_93(self):
        self.assertEqual([1, 2, 3, 4], [1, 2, 3, 4])

    def test_alina_misnik_fi_94(self):
        list = [3, 5, 2, 9, 8]
        self.assertEqual(delete(list), [3, 5, 2, 9])

    def test_andrii_kutsenko_fi_94(self):
        list1 = [4, 5, 7, 3, 8, 6, 3, 9]
        self.assertEqual(delete_element(list1), [4, 5, 7, 3, 6, 3, 9])

    def test_1_olia_futurska_fi94(self):
        listo1 = [1, 2, 3, 4, 5, 6, 7]
        listo2 = [1, 2, 3, 4, 6, 6, 7]
        self.assertIsNot(listo1[4], listo2[4])

    def test_kirill_kostiuk(self):
        self.assertEqual(len(['a', 'b'] + ['b']), 3)
        self.assertEqual(['a', 'b'] + ['b'], ['a', 'b', 'b'])

    def test_olena_velychko_fi_94(self):
        self.assertEqual(3 * [1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3])

    def test_illya_melnick_fi94(self):
        lista = [2, 2, 0, 9, 2, 0, 0]
        self.assertEqual(add_element(lista), [2, 2, 0, 9, 2, 0, 0, 1])

    def test_dmytro_moldovan_(self):
        self.assertEqual(len([]), 0)

    def test_Yelizaveta_Godovikova_FI94(self):
        list = ['a', 'k', 'j', 'y', 'r', 'o']
        self.assertEqual(del_third_element(list), ['a', 'k', 'y', 'r', 'o'])

    def test_Olya_Koroban_FI94(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(get_second_to_fifth_elements(a), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()
