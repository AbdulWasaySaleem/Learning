#Two sum is a classic problem where we need to find two numbers in an array that add up to a specific target.
def twoSum(nums, target):
    for i in range(len(nums)):
        result = target - nums[i]
        if result in nums[i+1:]:
            return i, nums.index(result, i + 1)

nums = [2, 7, 11, 15]
target = 17

indices = twoSum(nums, target)
print(f"indices of {target} are {indices[0]}, {indices[1]}")