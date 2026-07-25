class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for s in strs:
            t = [0] *26
            for c in s:
                t[ord(c)- ord("a")] +=1
            count1 = tuple(t)
            if count1 not in dict1:
                dict1[count1] = []
            dict1[count1].append(s) 
        

        return list(dict1.values())