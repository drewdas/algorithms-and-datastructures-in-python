import unittest
# arr = ['f', 'g','a', 'b', 'c', 'd', 'e']
# arr2 = ['c', 'd', 'e', 'f', 'g', 'a', 'b']


# 

def find_rotation_point(letters):
    first_letter = letters[0]
    floor_idx = 0
    ceiling_idx = len(letters)-1
    while floor_idx <= ceiling_idx:
        print(floor_idx, ceiling_idx)
        guess_idx = (floor_idx+ceiling_idx)//2
        if letters[guess_idx] < first_letter:
            ceiling_idx = guess_idx
        else:
            floor_idx = guess_idx
        
        
        if floor_idx + 1 == ceiling_idx:
            return ceiling_idx
        
    return -1


class TestCase(unittest.TestCase):
    def test_rotation_left(self):
        letters = ['f', 'g','a', 'b', 'c', 'd', 'e']
        expected = 2
        rotation_idx = find_rotation_point(letters)
        self.assertEqual(rotation_idx, expected)
    
    def test_rotation_right(self):
        letters = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
        expected = 5
        rotation_idx = find_rotation_point(letters)
        self.assertEqual(rotation_idx, expected)
    
    def test_two_elements(self):
        letters = ['b','a']
        expected = 1
        rotation_idx = find_rotation_point(letters)
        self.assertEqual(rotation_idx, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)