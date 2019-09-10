def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    k = k % length
    nums[:k], nums[k:] = nums[(length-k):], nums[:(length-k)]      