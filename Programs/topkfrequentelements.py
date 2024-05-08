from collections import defaultdict

nums = eval(input())
k = int(input())


# Bucket Sort
# create a array from 1 to n and store the elements of nums depending upon their frequency into it

count = {}
freq = [[] for i in range(len(nums)+1)]

for i in nums:
    count[i] = 1+ count.get(i,0) # If the number doesnt exist in the dict then return a default value of 0
for n,c in count.items():
    freq[c].append(n)
res = []
for i in range(len(freq)-1,0,-1 ):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)
