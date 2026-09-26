class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        i = 0
        while i < len(digits):
            sum = sum + digits[i]*(10**(len(digits)-i-1))    
            i += 1
            
        sum += 1
        digit_list = [int(digit) for digit in str(sum)]
        
        return digit_list
