class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre=[0]*len(nums)
        post = [0]*len(nums)
        r =[]

        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i]

        post[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            post[i]= post[i+1]*nums[i]
        
        for i in range(len(nums)):
            pe = i-1
            pt = i+1

            if not r:
                r.append(post[pt])
            elif len(post)>pt:
                m = pre[pe]*post[pt]
                r.append(m)
            else:
                r.append(pre[pe])


        return r


        # print(pre)
        # print(post)
            


            
            
            

        