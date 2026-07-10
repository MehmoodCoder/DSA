# class Solution:
#     def sortedSquares(self, num: List[int]) -> List[int]:
#         for i in range(len(num)):
#             num[i] = num[i]**2
#         return sorted(num)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = [0] * n  
        
        left = 0
        right = n - 1
        
        p = n - 1  
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[p] = left_square
                left += 1
            else:
                result[p] = right_square
                right -= 1
            p -= 1
            
        return result