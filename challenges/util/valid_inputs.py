def valid_inputs(nums):
    if not nums or type(nums) != list:
        return False
    if not all(isinstance(n, int) for n in nums):
        return False
    if any(n < 1 for n in nums):
        return False
    return True
