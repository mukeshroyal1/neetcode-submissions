class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            n = len(i)
            result += f'#{n}#{i}'

        return result 

    def decode(self, s: str) -> List[str]:
        result = []
        j = 0
        while j < len(s):
            if s[j] == "#":
                i = j+1
                num = ""
                while s[i] != "#":
                    num += s[i]
                    i += 1
                num2 = int(num)
                j = i + 1
                result.append(s[j:j+num2])
                j += num2
            
            else:
                break
        return result 



        