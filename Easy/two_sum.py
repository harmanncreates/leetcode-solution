# Pattern: Hashmap
# Time: O(n) | Space: O(n)
# Key insight: for each number, check if its complement
# (target - num) already exists in dictionary
# dictionary lookup is O(1) vs O(n) for nested loops

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
      for i, num in enumerate(nums) :
        diff = target - num 

        if diff in seen : 
            return [seen[diff],i]
        seen[num]=i
