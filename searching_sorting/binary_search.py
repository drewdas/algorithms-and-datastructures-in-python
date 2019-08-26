import unittest

def binary_search(array, value):
    # floor
    floor = 0
    # ceiling
    ceiling = len(array)-1
    # while loop to check it hasnt overlapped
    while floor <= ceiling:
        mid = (floor+ceiling)//2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            ceiling = mid-1
        else:
            floor=mid+1
    return -1

class Test(unittest.TestCase):
    def test_found(self):
        array = [112, 245, 339, 895, 1098, 1129, 1280]
        value = 895
        result = binary_search(array, value)
        expected = 3
        self.assertEqual(result, expected)

    def test_not_found(self):
        array = [112, 245, 339, 895, 1098, 1129, 1280]
        value = 1200
        result = binary_search(array, value)
        expected = -1
        self.assertEqual(result, expected)
    
    def test_not_found_low(self):
        array = [112, 245, 339, 895, 1098, 1129, 1280]
        value = 180
        result = binary_search(array, value)
        expected = -1
        self.assertEqual(result, expected)
    
    def test_not_in_range(self):
        array = [112, 245, 339, 895, 1098, 1129, 1280]
        value = 2000
        result = binary_search(array, value)
        expected = -1
        self.assertEqual(result, expected)
    
    def test_2_elements(self):
        array = [112, 245]
        value = 245
        result = binary_search(array, value)
        expected = 1
        self.assertEqual(result, expected)

    def test_2_elements_not_found(self):
        array = [112, 245]
        value = 0
        result = binary_search(array, value)
        expected = -1
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)