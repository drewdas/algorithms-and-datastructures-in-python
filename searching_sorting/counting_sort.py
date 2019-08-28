# You have create a very popular game.
# Each round, players receive a score between 0 and 100, which you use to rank them 
# from highest to lowest.
# Write a function that takes:
# a list of unsorted_scores and the highest_possible_score in the game
# and returns a sorted list of scores in less than O(n*lg n) time.
# We’re defining n as the number of unsorted_scores because we’re expecting 
# the number of players to keep climbing.
# And, we'll treat highest_possible_score as a constant instead of factoring it into our 
# big O time and space costs because the highest possible score isn’t going to change. 
# Even if we do redesign the game a little, the scores will stay around the same order of 
# magnitude.

#Brainstorm:
# We can use a counted sort here which will have an efficiency of O(n)
# initialize array with [None]*highest possible score call it scores
# iterate through unsorted score, use score value as index of scores array
# at the index set value to 1
# if score repeated add 1 to existing value
# iterate over unsorted array and use index as value where it 1 or more
# if more that add another to sorted
# reverse array and return

import unittest

def sort_scores(unsorted_scores, highest_possible_score):
    scores = [None] * highest_possible_score
    for i in unsorted_scores:
        if scores[i] == None:
            scores[i] = 1
        else:
            scores[i] += 1
    

    sorted_scores = []
    for i in range(len(scores)):
        if scores[i]:
            times = scores[i]
            t_count = 1
            while t_count <= times:
                sorted_scores.append(i)
                t_count += 1
    return sorted_scores[::-1]

class TestCase(unittest.TestCase):

    def test_case_1(self):
        unsorted_scores = [37, 89, 41, 65, 91, 53]
        HIGHEST_POSSIBLE_SCORE = 100
        sorted_scores = sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(sorted_scores, expected)
    
    def test_case_2(self):
        with self.assertRaises(IndexError):
            unsorted_scores = [101, 89, 2, 111, 200, 9, 9]
            HIGHEST_POSSIBLE_SCORE = 100
            sorted_scores = sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
    
    def test_case_3(self):
        unsorted_scores = [37, 89, 41, 1]
        HIGHEST_POSSIBLE_SCORE = 100
        sorted_scores = sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
        expected = [1, 37, 41, 89]
        self.assertEqual(sorted_scores, expected)
    
    





