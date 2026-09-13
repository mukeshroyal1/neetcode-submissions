class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        maxseq = 0
        for i in nums:
            temp = 1
            if (i-1) in check:
                continue 
            else:
                j = i
                while (j+1) in check:
                    temp += 1
                    j += 1
                maxseq = max(temp, maxseq)
        return maxseq

