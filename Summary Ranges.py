class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = i
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == i:
                result.append(str(nums[start]))
            else:
                result.append(f"{nums[start]}->{nums[i]}")
            i += 1

        return result
        
