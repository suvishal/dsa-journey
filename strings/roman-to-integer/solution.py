class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        n = len(s)
        i = 0

        while i<n:
            if i < n-1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                sum += roman_to_int[s[i+1]] - roman_to_int[s[i]]
                i +=2
            #elif i< n-1 and roman_to_int[s[i]] == roman_to_int[s[i+1]]:
                #sum += roman_to_int[s[i+1]]
                #i +=1
            else:
                sum += roman_to_int[s[i]]
                i +=1
        
        return sum

