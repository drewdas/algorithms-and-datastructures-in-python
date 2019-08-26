import unittest

def merge_ranges(meetings):
    # [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    #[(0,1), (3,8), (9,12)]

    # edge cases
    # [] then return []
    if not meetings:
        return []
    # create merged_meetings array
    merged_meetings = []
    # sort meetings by start time
    sorted_meetings = sorted(meetings)
    # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

    # add first meeting to merged_meetings
    merged_meetings.append(sorted_meetings[0])

    # iterate through sorted_meeting from second meeting
    for i in range(1, len(sorted_meetings)):
        # set current meeting
        current_start, current_end = sorted_meetings[i]
        # get last merged_meeting
        last_start, last_end = merged_meetings[-1]
        # if current start < or = end of last, then merge
        if current_start <= last_end:
            # merged = (last start, max(current end, last end))
            merged = (last_start, max(current_end, last_end))
            # replace last merged meeting
            merged_meetings[-1] = merged
        else:
            # else current start is greater than last end
            # add meeting to merged list
            merged_meetings.append((current_start, current_end))
    
    return merged_meetings
        

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)