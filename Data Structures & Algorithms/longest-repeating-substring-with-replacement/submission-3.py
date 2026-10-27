class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1 ={}

        left =0
        longest =0

        for r in range(len(s)):
            dict1[s[r]] = dict1.get(s[r],0) +1

            tempMax= max(dict1.values() )
            
            while ((r - left +1)-tempMax >k):
                dict1[s[left]] -=1
                left +=1
            longest = max(longest,r-left+1)
        return longest

