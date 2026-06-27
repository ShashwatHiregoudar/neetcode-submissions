class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_visit = {}

        for idx, val in enumerate(nums):
            diff = target - val
            try:
                _ = previous_visit[diff]
                return [previous_visit[diff], idx]
            except:
                previous_visit[nums[idx]] = idx
