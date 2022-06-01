# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}
        left = 0
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            
            while (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        return result