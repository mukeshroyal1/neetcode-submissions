class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tempS = {}
        tempT = {}
        for i in s:
            if i not in tempS:
                tempS[i] = 1
            else:
                tempS[i] += 1
        for j in t:
            if j not in tempT:
                tempT[j] = 1
            else:
                tempT[j] += 1
        if len(tempS) != len(tempT):
            return False
        for i in tempS:
            if i in tempT and tempT[i] == tempS[i]:
                continue 
            else:
                return False
        return True


    
        