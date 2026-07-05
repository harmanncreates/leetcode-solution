# Pattern: Hashmap / Character Count
# Time: O(n) | Space: O(1) — max 26 keys
# Key insight: count character frequencies in s,
# then verify t matches by decrementing counts
# early exit if lengths differ

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True   
