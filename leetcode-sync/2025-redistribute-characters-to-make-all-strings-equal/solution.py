class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if not words:
            return True

        char_count = {}
        
        # Count occurrences of each character
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
        
        # Check if each character count is divisible by the number of words
        n = len(words)
        for count in char_count.values():
            if count % n != 0:
                return False
        
        return True
