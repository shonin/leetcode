class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = collections.Counter(nums)
        values = list(nums.values())
        values.sort()
        values_needed = values[-k:]

        return [key for key, value in nums.items() if value in values_needed]
      
