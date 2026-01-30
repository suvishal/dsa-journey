class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        c_set = set()
        max_len = 0
        for j in range(len(s)):
            while s[j] in c_set:
                c_set.remove(s[i])
                i += 1

            c_set.add(s[j])
            max_len = max(max_len, j-i+1)
        return max_len
