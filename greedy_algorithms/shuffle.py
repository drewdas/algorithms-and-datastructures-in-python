# Write a function for doing an in-place shuffle of a list.
# The shuffle must be "uniform," meaning each item in the original 
# list must have the same probability of ending up in each spot in 
# the final list. Assume that you have a function 
# get_random(floor, ceiling) for getting a random integer that 
# is >= floor and <= ceiling.
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(arr):
    if len(arr) <= 1:
        return arr
    last_idx = len(arr) - 1
    for idx in range(len(arr)-2):
        random_idx = get_random(idx, last_idx)
        if random_idx != idx:
            arr[idx], arr[random_idx] = arr[random_idx], arr[idx]




sample_list = [x for x in range(1,15)]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)