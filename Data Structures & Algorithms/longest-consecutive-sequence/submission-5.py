class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A = set(nums)
        highest = 0
        for i in A:
            current = i
            count = 1;
            if current-1 not in A:
                while current+1 in A:
                    current+=1
                    count+=1
                if highest< count:
                    highest = count
        
        return highest
