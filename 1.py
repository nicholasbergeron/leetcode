nums = [3,2,4]
target = 6

def solution(nums, target):
    n_nums = len(nums)

    for i in range(n_nums):
        for j in range(n_nums):
            if i != j and nums[i] + nums[j] == target:
                return [i,j]
print(solution(nums, target))
