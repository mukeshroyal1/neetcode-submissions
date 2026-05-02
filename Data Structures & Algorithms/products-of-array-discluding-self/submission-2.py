class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[0])
                continue 
            temp = nums[i] * prefix[-1]
            prefix.append(temp)
        for i in range(len(nums)-1, 0, -1):
            if i == len(nums)-1:
                postfix.append(nums[-1])
                continue 
            temp = nums[i] * postfix[0]
            postfix.insert(0, temp)
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[0])
            elif i == len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * postfix[i])
        
        return result

                
    


    