# This function performs a binary search algorithm on a sorted list of numbers.
def BinarySearch(nums, target):
    l, r = 0, len(nums)-1  # Set the leftmost and rightmost indices of the list.

    # Perform binary search as long as the left index is less than or equal to the right index.
    while l <= r:
        mid = (l + r) // 2  # Calculate the middle index.

        # If the middle element of the list is greater than the target, adjust the right index.
        if nums[mid] > target:
            r = mid - 1
        # If the middle element is less than the target, adjust the left index.
        elif nums[mid] < target:
            l = mid + 1
        # If the middle element equals the target, return the index.
        else:
            return mid

    return -1  # Return -1 if the target is not found in the list.

# Test the BinarySearch function with user input list and target.
print(BinarySearch(eval(input()), int(input())))
