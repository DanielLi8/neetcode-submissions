class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        best = 0
        longest= 1

        sort1= sorted(nums)
        print(sort1)
        for i in range(len(sort1)-1):
            if sort1[i] +1 ==sort1[i+1]:
                longest+=1
                print(sort1[i])
            elif sort1[i] == sort1[i+1]:
                continue
            else:
                if best<longest:
                    best = longest
                longest = 1
                print(best)

        if best<longest:
            best = longest
                
    
        return best
        