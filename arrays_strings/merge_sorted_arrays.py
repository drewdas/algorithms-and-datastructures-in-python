# Merging Sort Arrays

# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.

# Constraints:
# Do it in one pass without using in-built sorted() function

# edge cases:
# one of the lists can be shorter than the other

import unittest

def merge_lists(list1, list2):
    sorted_list_length = len(list1) + len(list2)
    sorted_list = [None] * sorted_list_length

    current_list1_idx = 0
    current_list2_idx = 0
    current_sorted_idx = 0
    while  current_sorted_idx < sorted_list_length:
        is_list1_exhausted = False
        is_list2_exhausted = False

        # check if list1 is exhausted
        if current_list1_idx >= len(list1):
            is_list1_exhausted = True
        # check if list2 is exhausted
        if current_list2_idx >= len(list2):
            is_list2_exhausted = True

        # if list 1 is not  exhausted and either list 2 is exhausted 
        # or the first unmerged element in list 1 is smaller than in list 2 
        if (not is_list1_exhausted and (is_list2_exhausted or \
            list1[current_list1_idx] < list2[current_list2_idx])):
            sorted_list[current_sorted_idx] = list1[current_list1_idx]
            current_list1_idx += 1
        else:
            # if list 1 is exhausted
            sorted_list[current_sorted_idx] = list2[current_list2_idx]
            current_list2_idx += 1
        
        current_sorted_idx += 1
    
    return sorted_list

class TestCase(unittest.TestCase):
    def test_case_1(self):
        list1 = [3, 4, 6, 10, 11, 15]
        list2 = [1, 5, 8, 12, 14, 19]
        expected = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
        result = merge_lists(list1, list2)
        self.assertEqual(result, expected)

    def test_case_2(self):
        list1 = [2, 10, 15]
        list2 = [1, 3, 12, 14, 19]
        expected = [1, 2, 3, 10, 12, 14, 15, 19]
        result = merge_lists(list1, list2)
        self.assertEqual(result, expected)

    def test_case_3(self):
        list1 = [1, 3, 12, 14, 19]
        list2 = [2, 10, 15]
        expected = [1, 2, 3, 10, 12, 14, 15, 19]
        result = merge_lists(list1, list2)
        self.assertEqual(result, expected)

# Brainstorming
# [3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19], []
# iterate over list 1
# compare value from list 1 to list 2 and add lesser value to sorted list
# remember elements that not have been merged,
# move to next element in both list that have not been merged
# if index does not exist in list 2 add rest of list 1 to sorted list
# otherwise add rest of list 1 to sorted array
# 3 1, add 1 to []
# 3 5, add 3 to [1]
# 4 5, add 4 to [1, 3]
# 6 5, add 5 to [1, 3, 4]
# and so on...

