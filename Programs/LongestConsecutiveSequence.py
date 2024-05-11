
def longestConsecutiveSequence(sequence):
    longest = 0
    num_set = set(sequence)

    for n in num_set:
        if (n-1) not in num_set:
            length = 1
            while (n+length) in num_set:
                length +=1 
            longest = max(longest, length)
    return longest


