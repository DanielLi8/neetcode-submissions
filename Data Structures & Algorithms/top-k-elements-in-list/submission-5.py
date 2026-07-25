import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1= {}

        for n in nums:
            dict1[n] =dict1.get(n,0)+1
        
        arr=[]
        for num, freq in dict1.items():
            arr.append([freq,num])
        arr.sort()

        res=[]
        while len(res) <k:
            res.append(arr.pop()[1])
        return res

