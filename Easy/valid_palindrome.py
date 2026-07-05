# Pattern: Two Pointers
# Time: O(n) | Space: O(1)
# Key insight: skip non-alphanumeric characters in place
# compare left and right moving inward
# O(1) space vs O(n) for creating new cleaned string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for char in s:
            if char.isalnum():
                clean += char.lower()

        for i in range(len(clean) // 2):
            if clean[i] != clean[-i - 1]:
                return False

              return True      # creates new string O(n) not very efficient time; O(n) 


      

          class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True         #O(1) better no new string for interview 

              
