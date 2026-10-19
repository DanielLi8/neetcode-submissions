class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr =""

        for ch in s:

            while ch in curr:
                curr = curr[1:]
            
            curr +=ch

            longest = max(longest,len(curr))

        
        return longest