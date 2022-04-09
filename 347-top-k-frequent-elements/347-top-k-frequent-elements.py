from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        l = []
        for i in d.most_common():
            l.append(i[0])
        return l[:k]