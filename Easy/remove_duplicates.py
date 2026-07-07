time complexity: O(n)
space complexity: O(1)
key idea:left:where unique no. should be placed
right: scans array
comp. current no. with last unique no.nums[left-1]
if diff. copy current one to left then move left
  


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       if not nums:
          return 0
       left = 1
       
       for right in range(1, len(nums)):
           if nums[right] != nums[left - 1]:
             nums[left] = nums[right]
             left += 1
       return left
              
