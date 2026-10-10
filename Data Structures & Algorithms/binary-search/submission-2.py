class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i_min = 0 
        i_max = len(nums)-1
        while i_max>=i_min:
            
            i = (i_min + i_max)//2
            print(i)
            if nums[i] == target:
                return i 
            if nums[i]>target:
                i_max = i-1
            else:
                i_min = i+1 

        return -1
        