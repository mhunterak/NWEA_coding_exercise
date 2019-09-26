import unittest
from flatten_array import flatten


class TestFlattenArray(unittest.TestCase):
    def setUp(self):
        self.input_array_1 = [1, 2, [3]]
        self.input_array_2 = [1, 2, 3, [[4, [5], 6]]]
        self.input_array_3 = [1, 2, 3, [4, 5, 6], 7, 8]
        self.input_array_4 = [1, [[[[[[2]]]]]], 3, [4, [5, 6]], 7, 8, [9, 10]]
        self.input_array_5 = [
            [1], [2, [3]], [[[4], 5], [6]], [[7], 8], [9, 10]]

    def test_case1(self):
        assert flatten(self.input_array_1) == [1, 2, 3]

    def test_case2(self):
        assert flatten(self.input_array_2) == [1, 2, 3, 4, 5, 6]

    def test_case3(self):
        assert flatten(self.input_array_3) == [
            1, 2, 3, 4, 5, 6, 7, 8]

    def test_case4(self):
        assert flatten(self.input_array_4) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_case5(self):
        assert flatten(self.input_array_5) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_case6(self):
        assert flatten([]) == []

    def test_case7(self):
        with self.assertRaises(TypeError):
            flatten([2, 'b'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlattenArray)
    unittest.TextTestRunner(verbosity=2).run(suite)
