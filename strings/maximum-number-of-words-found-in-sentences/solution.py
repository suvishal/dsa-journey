class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_length_of_words = 0
        i = 0
        for i in range(len(sentences)):
             for word in sentences:
                     max_length_of_words = max(max_length_of_words, len(word.split()))
    
        return max_length_of_words
