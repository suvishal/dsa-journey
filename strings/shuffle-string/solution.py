class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        letters = list(s)
        t  = ['']* len(indices)
        for i in range(len(indices)):
            t[indices[i]] = letters[i]
        return ''.join(t)       


