class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in nums:
            if i not in result:
                result[i] = 0
            result[i] += 1
        
        final = sorted(result.items(), key=lambda t: t[1], reverse=True)
        frelist = []
        for i in range(k):
            frelist.append(final[i][0])
        return frelist

            