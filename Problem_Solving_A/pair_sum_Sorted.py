# Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

# Example 1:
# Input: nums = [-5, -2, 3, 4, 6], target = 7
# Output: [2, 3]
# Explanation: nums[2] + nums[3] = 3 + 4 = 7

# Example 2:
# Input: nums = [1, 1, 1], target = 2
# Output: [0, 1]
# Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].


def find_pair(nums, target):
    left, right = 0, len(nums) - 1
    result = []

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            result.append([left, right])
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return result if result else []

# ✅ Test cases
test1 = find_pair([-5, -2, 3, 4, 6], 7)   # Expected: [[2, 3]]
test2 = find_pair([1, 1, 1], 2)           # Expected: multiple valid outputs

# Print results
print("Test 1:", test1)
print("Test 2:", test2)
