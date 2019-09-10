import unittest

def highest_product_of_3(arr_of_ints):

    if len(arr_of_ints) < 3:
        return None

    # we keep track of highest, lowest, highest_product_of_2
    # lowest_product_of_2 and highest_product_of_3

    # initialize with first 3 elements

    highest_product_of_2 = arr_of_ints[0]*arr_of_ints[1]
    lowest_product_of_2 = arr_of_ints[0]*arr_of_ints[1]
    highest_product_of_3 = arr_of_ints[0]*arr_of_ints[1]*arr_of_ints[2]

    highest = max(arr_of_ints[0], arr_of_ints[1])
    lowest = min(arr_of_ints[0], arr_of_ints[1])

    for i in range(2, len(arr_of_ints)):
        current = arr_of_ints[i]

        # highest of 3
        highest_product_of_3 = max(highest_product_of_3,
                                   current*highest_product_of_2,
                                   current*lowest_product_of_2)
        # highest of 2
        highest_product_of_2 = max(highest_product_of_2,
                                   current*highest,
                                   current*lowest)
        
        # lowest of 2
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current*highest,
                                  current*lowest)

        # lowest
        lowest = min(current, lowest)

        # highest
        highest = max(current, highest)

    return highest_product_of_3

class TestCase(unittest.TestCase):
    def test_case_1(self):
        arr = [3, 4, 5]
        result = highest_product_of_3(arr)
        expected = 60
        self.assertEqual(result, expected)

    def test_case_2(self):
        arr = [3, 8, 5, 4, 10]
        result = highest_product_of_3(arr)
        expected = 400
        self.assertEqual(result, expected)

    def test_case_3(self):
            arr = [3, 8, 5, 4, 10, -100, -20, 1, -2]
            result = highest_product_of_3(arr)
            expected = 20000
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)