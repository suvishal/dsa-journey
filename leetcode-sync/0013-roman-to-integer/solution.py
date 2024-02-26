class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        previous_ans = 0
        i = 0
        while i < len(s):
            if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i - 1]]:
                ans += roman_to_int[s[i]] - 2 * roman_to_int[s[i - 1]]
            else:
                ans += roman_to_int[s[i]]
            i += 1
        return ans

