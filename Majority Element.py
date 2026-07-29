class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0 
        numb = None
        for num in nums:
            if c == 0:
                numb = num
            c += 1 if num == numb else -1
        return numb
        
