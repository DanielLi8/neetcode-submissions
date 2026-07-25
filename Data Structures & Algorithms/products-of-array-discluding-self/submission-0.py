class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,i= [],0

        while i<len(nums):
            prod= 1
            for s in range(len(nums)):
                if s == i:
                    continue
                else:
                    prod = prod * nums[s]
            res.append(prod)
            i+=1
        
        return res
