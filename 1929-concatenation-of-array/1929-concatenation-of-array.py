class Solution:
    def getConcatenation(self, nums):
        
        ans = []

        for i in range(len(nums)):
            ans.append(nums[i]) 
    
        for i in range(len(nums)):    
            ans.append(ans[i])
        return ans  

        # simple 

        # return nums+nums 

        # return 2*nums