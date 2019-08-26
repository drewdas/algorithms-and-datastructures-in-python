import unittest

def reverse(list_of_chars):
    # to reverse in place swap first and last
    # swap second and second to last
    # until reached middle

    # set left index to first element
    # set right index to last element
    # [1,2,3,4,5]
    # [5,2,3,4,1]
    # [5,4,3,2,1]

    # cases
    # empty list
    if list_of_chars == []:
        return []

    left_index = 0
    right_index = len(list_of_chars) - 1
    # if left_index and right index overlap
    while left_index < right_index:
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        left_index += 1
        right_index -= 1
    return list_of_chars

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)