def minEatingSpeed(piles, h) -> int:
    l, r = 1, max(piles)
    
    def isSufficientSpeed(cnt):
        return sum(ceil(i/cnt) for i in piles) <= h

    while l < r:
        m = (l + r)//2
        if isSufficientSpeed(m):
            r = m