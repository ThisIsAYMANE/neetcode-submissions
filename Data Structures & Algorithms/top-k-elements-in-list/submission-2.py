class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num={}
        for x in nums:
                num[x] = num.get(x, 0) + 1
        resultat=sorted(num, key=num.get, reverse=True)
        return resultat[:k]
        