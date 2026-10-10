class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        f = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for j in t:        
           f[j] = f.get(j, 0) + 1        
        return d==f
         
            
        