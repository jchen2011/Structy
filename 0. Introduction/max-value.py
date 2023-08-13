def max_value(nums):
    highest = nums[0]

    for x in nums:
        if x > highest:
            highest = x

    return highest
