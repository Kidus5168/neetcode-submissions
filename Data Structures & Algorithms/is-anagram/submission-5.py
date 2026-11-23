from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        fw = {}
        sw = {}

        for i in range(len(s)):
            fw[s[i]] = fw.get(s[i],0)+1
            sw[t[i]] = sw.get(t[i],0)+1
        return fw == sw 

        