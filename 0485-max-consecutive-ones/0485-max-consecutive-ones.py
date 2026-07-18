class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max1s = 0
        for i in nums:
            if i == 1:
                counter += 1
                if counter > max1s:
                    # max1s += 1
                    max1s = counter
            else:
                counter = 0
        return max1s

