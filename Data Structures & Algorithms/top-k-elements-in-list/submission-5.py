class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        result = []
        
        for i in range(k):
            max = ""
            for i in freq:
                if max == "" or freq[i] >= freq[max]:
                    max = i
            result.append(max)
            freq[max] = 0
        return result
            


        

       


