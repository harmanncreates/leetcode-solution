# Maximum Subarray
## Pattern = Kadane's Algorithm
## Time Complexity = O(n)
## Space Complexity = O(1)
## Key Idea = At every element, choose the better option:
- Start a new subarray.
- Continue the current subarray.
## What I Learned = Kadane's Algorithm tracks the best subarray ending at the current index.


  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
             
