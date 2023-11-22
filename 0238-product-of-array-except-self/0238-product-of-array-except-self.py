class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        preFix = [1] * len(nums)
        
        for i in range(1,len(nums)):
            preFix[i] = preFix[i-1] * nums[i-1]
            
        right = 1
        
        for i in range(len(nums) - 2, -1 , -1):
            right *= nums[i + 1]

            preFix[i] = preFix[i] * right
            
        preFix[0] = right
            
        return preFix