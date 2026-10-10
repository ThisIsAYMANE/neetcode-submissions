class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)                 # {num: frequency}
        top = count.most_common(k)            # [(num, freq), ...] highest freq first
        return [num for num, freq in top]   
        