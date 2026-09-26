class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        i = 1
        while i  < len(mountain)-1:
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                peaks.append(i)
            i += 1
        return peaks

