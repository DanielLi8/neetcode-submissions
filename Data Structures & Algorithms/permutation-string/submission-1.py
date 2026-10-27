class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = {}
        windowSize = len(s1)
        for char in s1:
            s1Hash[char] = s1Hash.get(char,0) +1

        s2Hash ={}
        left = 0
        

        for right in range(len(s2)):
            s2Hash[s2[right]] = s2Hash.get(s2[right],0) + 1
            
            while ((right -left +1) > windowSize):
                s2Hash[s2[left]] -=1
                if s2Hash[s2[left]] == 0:
                    s2Hash.pop(s2[left])
                left +=1
            
            
            if s2Hash == s1Hash :
                return True
        
        return False
