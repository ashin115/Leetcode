def commonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, s in enumerate(shortest):
        for other in strs:
            if other[i] != s:
                return shortest[:i]
    return shortest
