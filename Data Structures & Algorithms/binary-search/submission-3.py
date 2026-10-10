
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new = nums
        position = 0

        while len(new) > 0:
            mid = len(new) // 2

            if target == new[mid]:
                return position + mid

            elif target > new[mid]:
                position += mid + 1
                new = new[mid + 1:]

            else:
                new = new[:mid]

        return -1