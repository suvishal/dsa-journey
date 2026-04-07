## Contains Duplicate

    seen =set()
        for i, n in enumerate(nums):
            if n in seen:
                return True
            seen.add(n)
        return False

#why seen set over dict? since we don't need to use memory for loaction we just have to know if it is repeated so we go for a completely unordered datatype
