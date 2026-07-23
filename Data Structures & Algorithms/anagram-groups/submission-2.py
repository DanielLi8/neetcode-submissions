from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
    
        for s in strs:
            t="".join(sorted(s))
            dict1[t].append(s)

        print(dict1.values())
        return list(dict1.values())