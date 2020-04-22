class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#First try didnt work so we continue
        
#         res = []
#         for i in range(len(nums)):
#             res.append(reduce((lambda x, y: x * y),nums[:i]+nums[i+1:] ))            
#         return res   

        left = [1] * len(nums)
        right = [1] * len(nums)
        res = []

        for i in range(len(nums)-1):
            left[i+1]*= left[i]*nums[i]

        for i in range(len(nums)-1, 0, -1):
            right[i-1]*= right[i]*nums[i]

        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res

    
    
