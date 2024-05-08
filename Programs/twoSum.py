def twoSum( nums, target):
    dict={}
    for i,n in enumerate(nums):
        if n in dict:
            return dict[n],i
        else:
            dict[target-n]=i

nums = eval(input())
target = int(input())

print(twoSum(nums,target))