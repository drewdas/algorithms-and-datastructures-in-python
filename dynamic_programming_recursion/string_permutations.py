import unittest

# Write a recursive function for generating all permutations 
# of an input string. Return them as a set.

# abc
# cab
# acb


# Brain Storm
# recursively get all permutations of string except last
# take the last character
# move its position across the string
# ex: cats, scat, csat, cast
# ex: cat, cta, tca, act, atc.. and do same thing with s: scta csta ctsa...

def get_permutations(string):
    # check if len(string) < 2
    if len(string) < 2:
        return set([string])
    
    # all characters except last
    all_chars_except_last = string[:-1]
    # last character
    last_char = string[-1]

    all_permutations_except_last_char = get_permutations(all_chars_except_last)
    permutations = set()

    for permutation_except_last_char in all_permutations_except_last_char:
        for position in range(len(permutation_except_last_char)+1):
            permutation = permutation_except_last_char[:position] + last_char + permutation_except_last_char[position:]
            permutations.add(permutation)
    return permutations


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    p = get_permutations('abc')
    print(p)
    # unittest.main(verbosity=2)

