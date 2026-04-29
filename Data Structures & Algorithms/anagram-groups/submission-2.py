class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in strs:
            key = [0] * 26
            for j in i:
                key[ord(j) - ord('a')] += 1
            key = tuple(key)
            if key not in result:
                result[key] = []
            result[key].append(i)
        return list(result.values())

        
        