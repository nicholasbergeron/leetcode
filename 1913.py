def maxProductDifference(nums):
    w = max(nums)
    w_index = nums.index(w)
    nums = nums[:w_index] + nums[w_index+1:]
    x = max(nums)
    
    y = min(nums)
    y_index = nums.index(y)
    nums = nums[:y_index] + nums[y_index+1:]
    z = min(nums)

    return w*x - y*z

test_array = [7,6,4,2,3] # should get 7*6 - 2*3 = 42-6=36
print(test_array)
print(maxProductDifference(test_array))