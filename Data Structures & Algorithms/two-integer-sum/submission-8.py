class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = -1
        num2 = -1
        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums[i+1:]:
                num1 = i
                break 
        for i in range(len(nums[num1:])):
            if nums[num1+i] + nums[num1] == target:
                num2 = num1+i
        return [num1, num2]
