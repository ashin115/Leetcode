# Function to calculate product of array except self
def productOfArrayExceptSelf(nums):
    length = len(nums)
    sol = [1] * length
    pre = 1
    post = 1
    for i in range(length):
        sol[i] *= pre
        pre = pre * nums[i]
        sol[length - i - 1] *= post
        post = post * nums[length - i - 1]
    return sol


print(productOfArrayExceptSelf(eval(input())))
