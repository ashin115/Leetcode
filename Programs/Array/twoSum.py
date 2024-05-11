# Two Sum: Given an array of integers and a target sum,
# find two elements in the array that add up to the target sum.


def twoSum(nums, target):
    # Create an empty dictionary to store the indices of the numbers.
    dict = {}

    # Iterate over the input list of numbers.
    for i, n in enumerate(nums):
        # Check if the current number is already in the dictionary.
        if n in dict:
            # If it is, return the index and value of the two numbers that add up to the target sum.
            return [dict[n], i]

        else:
            # If not, add the difference between the target sum and the current number to the dictionary.
            dict[target - n] = i

