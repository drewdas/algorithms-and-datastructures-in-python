# There are two registers: one for take-out orders, and the other for the other folks 
# eating inside the cafe. All the customer orders get combined into one list for the 
# kitchen, where they should be handled first-come, first-served.

# Given all three lists, write a function to check that my service is first-come, 
# first-served. All food should come out in the same order customers requested it.

# Take Out: [1,5,8,10,11]
# Dine In: [2,3,4,6,7,9]

# Valid
# Served: [1,2,5,8,3,4,6,10,11,7,9]

# Invalid 
# Served: [1,2,3,8,5,6...]

# Cases:
# Equal Lists
# Unequal Lists
# 1 Empty List
# Unserved Orders


# Brainstorming
# iterate through served orders
# track three indexes: current_idx, last_served_take_out_idx, last_served_dine_in_idx



import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True


# Tests

class Test(unittest.TestCase):
    # equal order lists
    def test_case_1(self):
        take_out_orders = [1,5,8,10,11]
        dine_in_orders = [2,3,4,6,7,9]
        served_orders = [1,2,5,8,3,4,6,10,11,7,9]
        self.assertTrue(is_first_come_first_served(take_out_orders, dine_in_orders, served_orders))
    
    # unequal orders lists
    def test_case_2(self):
        take_out_orders = [1,5,8]
        dine_in_orders = [2,3,4,6,7]
        served_orders = [1,2,3,5,8,4,6,7]
        self.assertTrue(is_first_come_first_served(take_out_orders, dine_in_orders, served_orders))

    # not first come first served
    def test_case_3(self):
        take_out_orders = [1,5,6]
        dine_in_orders = [2,3,4]
        served_orders = [1,3,5,6,2]
        self.assertFalse(is_first_come_first_served(take_out_orders, dine_in_orders, served_orders))

    # empty list
    def test_case_4(self):
        take_out_orders = []
        dine_in_orders = [2,5,6]
        served_orders = [2,5,6]
        self.assertTrue(is_first_come_first_served(take_out_orders, dine_in_orders, served_orders))

if __name__ == '__main__':
    unittest.main(verbosity=2)





















#   def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
#     take_out_orders_index = 0
#     dine_in_orders_index = 0
#     take_out_orders_max_index = len(take_out_orders) - 1
#     dine_in_orders_max_index = len(dine_in_orders) - 1

#     for order in served_orders:
#         # If we still have orders in take_out_orders
#         # and the current order in take_out_orders is the same
#         # as the current order in served_orders
#         if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
#             take_out_orders_index += 1

#         # If we still have orders in dine_in_orders
#         # and the current order in dine_in_orders is the same
#         # as the current order in served_orders
#         elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
#             dine_in_orders_index += 1

#         # If the current order in served_orders doesn't match the current
#         # order in take_out_orders or dine_in_orders, then we're not serving first-come,
#         # first-served.
#         else:
#             return False

#     # Check for any extra orders at the end of take_out_orders or dine_in_orders
#     if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
#         return False

#     # All orders in served_orders have been "accounted for"
#     # so we're serving first-come, first-served!
#     return True

# Tests
