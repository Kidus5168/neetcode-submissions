class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        r = {}

        for i , n in enumerate(nums):
            r[n] = i
        # print(r)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in r and r[diff]!= i:
                return[i,r[diff]]

       

        