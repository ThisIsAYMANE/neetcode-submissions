import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)      # first index where nums[i] >= target
        if i < len(nums) and nums[i] == target:   # in range AND actually equal
            return i
        return -1