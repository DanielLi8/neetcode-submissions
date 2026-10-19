class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1={}
        left=0
        longest = 0

        for right in range(len(s)):
            dict1[s[right]] = dict1.get(s[right],0)+1

            maxValue = max(dict1.values())

            while( (right-left)-maxValue == k):
                dict1[s[left]] -=1
                left +=1
                maxValue = max(dict1.values())

            longest = max(longest,(right-left+1))
        return longest


                






