from challenges.util.valid_inputs import valid_inputs


def find_duplicate(nums):
    if not valid_inputs(nums):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return nums[i]

    return False
