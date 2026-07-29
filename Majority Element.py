class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            c = 0

            for j in range(n):
                if nums[i] == nums[j]:
                    c += 1
            
            if c > n // 2:
                return nums[i]
        
        return -1

        
