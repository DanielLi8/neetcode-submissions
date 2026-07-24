class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        t = ["".join(sorted(s))for s in strs]
        
        dict1={}

        for i in range(len(strs)):
            if t[i] not in dict1:
                dict1[t[i]]= []
            dict1[t[i]].append(strs[i])

        return list(dict1.values())

            