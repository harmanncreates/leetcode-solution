# Pattern: Two Pointers
# Time: O(n) | Space: O(1)
# Key insight: sorted array lets us exploit order
# sum too small → move left pointer right
# sum too big → move right pointer left
# no hashmap needed — more space efficient than Two Sum I

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1
