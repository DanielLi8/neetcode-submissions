class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortList = sorted(nums)
        final=[]


        for i in range(len(sortList)-1):
            curr = i
            left =i+1
            right = len(sortList)-1
            
            if i>0 and sortList[curr] == sortList[curr - 1]:
                continue
            
            while left < right:
                currSum= sortList[left] + sortList[right] + sortList[curr]

                if currSum == 0:
                    final.append([sortList[curr], sortList[left], sortList[right]])
                    left+=1
                    right-=1
                    while left < right and sortList[left] == sortList[left-1]   :
                        left+=1
                    while left < right and sortList[right]== sortList[right+1]:
                        right-=1
                elif currSum > 0:
                    right -=1
                elif currSum < 0:
                    left +=1
                
            print(final)
        return final

        