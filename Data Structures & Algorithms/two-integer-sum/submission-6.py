class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = -1
        temp = -1
        l = -1
        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums[i+1:]:
                j = i
                temp = find
                
        for k in range(j+1, len(nums)):
            if nums[k] == temp:
                l = k
                break
        return [j, l]

        
