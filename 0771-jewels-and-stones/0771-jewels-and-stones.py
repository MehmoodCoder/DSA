class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # counter = 0
        # for jewel in jewels:
        #     for stone in stones:
        #         if jewel == stone:
        #             counter += 1
        # return counter

# Optimal 1

        # count = 0
        # for i in stones:
        #     if i in jewels:
        #         count += 1 
        # return count     


# Optimal 2


        jewel_set = set(jewels)
        count = 0
        
        for stone in stones:
            if stone in jewel_set:
                count += 1
                
        return count   
        