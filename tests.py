import unittest
from flatten_array import flatten


class TestFlattenArray(unittest.TestCase):
    """
    Tests the fatten function various nested lists conditions
    """
    def setUp(self):
        '''
        Set up the tests with different condition variables
        '''
        self.input_array_int_list= [1, 2, 3]
        self.input_array_nested_list = [1, 2, 3, [[4, [5], 6]]]
        self.input_array_nested_list2 = [1, 2, 3, [4, 5, 6], 7, 8]
        self.input_array_nested_list3 = [1, [[[[[[2]]]]]], 3, [4, [5, 6]], 7, 8, [9, 10]]
        self.input_array_nested_list4 = [
            [1], [2, [3]], [[[4], 5], [6]], [[7], 8], [9, 10]]

    def test_int_list(self):
        assert flatten(self.input_array_int_list) == [1, 2, 3]

    def test_nested_list(self):
        assert flatten(self.input_array_nested_list) == [1, 2, 3, 4, 5, 6]

    def test_nested_list3(self):
        assert flatten(self.input_array_nested_list2) == [
            1, 2, 3, 4, 5, 6, 7, 8]

    def test_nested_list4(self):
        assert flatten(self.input_array_nested_list3) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_nested_list5(self):
        assert flatten(self.input_array_nested_list4) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_empty_list(self):
        assert flatten([]) == []

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            flatten([2, 'b'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlattenArray)
    unittest.TextTestRunner(verbosity=2).run(suite)
