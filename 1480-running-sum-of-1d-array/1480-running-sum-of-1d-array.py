# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         Running_sum = []
#         for i in range(len(nums)):
#             counter = 0
#             for j in range(1+i):
#                 counter += nums[j]
#             Running_sum.append(counter)
            
#         return Running_sum




# Second method 




class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

