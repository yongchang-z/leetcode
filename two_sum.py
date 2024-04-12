"""
Description:
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
You can return the answer in any order.
"""
from time_trials import time_trials

# Intuitive Solution 
def two_sum(nums, target):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [j, i]

# Optimized Solution
def two_sum_optimized(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

test_cases = {
    9: [2, 5, 7, 9],
    3: [1, 2, 3],
    6: [3, 2, 4],
    10: [1, 3, 5, 7]
}
print("{:<55}{}".format("two_sum", "two_sum_optimized"))
for n in [50, 100, 200, 400, 800, 1600, 3200]:
    nums = list(range(n))
    target = nums[-1] + nums[-2]
    time_trials(two_sum, nums, target, trials = 10)
    print("{:^20}".format("<--->"), end="")
    time_trials(two_sum_optimized, nums, target, trials = 10)
    print()
