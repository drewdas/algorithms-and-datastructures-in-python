# Your quirky boss collects rare, old coins...
# They found out you're a programmer and asked you to solve something 
# they've been wondering for a long time.

# Write a function that, given:

#     an amount of money
#     a list of coin denominations

# computes the number of ways to make the amount of money with coins of 
# the available denominations.

# Example: for amount=444 (444¢) and 
# denominations=[1,2,3][1,2,3][1,2,3] (111¢, 222¢ and 333¢), 
# your program would output 444—the number of ways to make 444¢ 
# with those denominations:

#     1¢, 1¢, 1¢, 1¢
#     1¢, 1¢, 2¢
#     1¢, 3¢
#     2¢, 2¢

import unittest

def change_possibilities(amount, denominations):

    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:

        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += (
                ways_of_doing_n_cents[higher_amount_remainder]
            )

    return ways_of_doing_n_cents[amount]

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, [1, 2, 3])
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, [1, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, [])
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, [25, 50])
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, [5, 10])
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, [1, 5, 10, 25, 50])
        expected = 292
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)