class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = sorted(nums)
        r = 1
        c = 1

        for i in range(1,len(n)):
            if  n[i-1] == n[i]:
                continue
            elif n[i] - n[i-1]==1:
                c+=1
            else:
                c=1
            r = max(c,r)  

        return r