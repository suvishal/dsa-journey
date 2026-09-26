class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = 0   
        i = 0
        while i < len(hours):
            if hours[i] >= target :
                c += 1
            i += 1
        return c
