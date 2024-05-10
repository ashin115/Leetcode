# This function finds the maximum area of a container that can be filled with water.
def maxArea(height):
     # Initialize the result (maximum area) to 0.
    res = 0
    
     # Initialize two pointers, one at the start and one at the end of the height array.
    l, r = 0, len(height)-1
    
     # Loop until the two pointers meet (i.e., the container is full).
    while l < r:
         # Calculate the area of the container that can be filled with water between the two pointers.
        area = (r-l) * min(height[l], height[r])
        
         # Update the result to be the maximum of the current result and the calculated area.
        res = max(area, res)
        
         # Move the pointer with the smaller height closer to the other pointer.
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

     # Return the maximum area that can be filled with water.
    return res

# Read in a list of heights from user input and call the maxArea function with it, then print the result.
print(maxArea(eval(input())))
