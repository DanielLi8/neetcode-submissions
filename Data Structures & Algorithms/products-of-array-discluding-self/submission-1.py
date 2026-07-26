class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,i= [],0
        zeroPresent=0
        prod = 1
        for num in nums:
            if num == 0:
                zeroPresent+=1
                continue
            else:
                prod *=num
        
        for num in nums:
            if zeroPresent == 1:
                if num != 0:
                    res.append(0)
                elif num == 0:
                    res.append(prod)
            elif zeroPresent>1:
                res.append(0)
            else:
                res.append(prod//num)
        
        return res