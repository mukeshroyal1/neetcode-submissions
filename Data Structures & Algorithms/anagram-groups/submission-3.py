class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            count = ''.join(str(count))
            if count in result:
                result[count].append(i)
            else:
                result[count] = [i]
        return list(result.values())
            
        