class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        groups = {}
        for i in freq:
            if freq[i] in groups:
                groups[freq[i]].append(i)
            else:
                groups[freq[i]] = [i]
        result = [0] * (len(nums) + 1)
        for i in range(len(result)):
            if i in groups:
                result[i] = groups[i]
        answer = []
        for i in range(len(result)-1, -1, -1):
            if (type(result[i]) == int) and (result[i] != 0):
                answer.append(result[i]) 
            elif type(result[i]) == list:
                answer.extend(result[i])
            if len(answer) == k:
                break 
        return answer 

        

       

# so bascially I need to group numbers based on their frequencey. So I can get tthe frequency of each of the numbers and treat the values as the keys and the key's as the values. 

