def bisect_left(nums, val):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l

def bisect_right(nums, val):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= val:
            l = mid + 1
        else:
            r = mid 
    return l

# TESTS

nums = [1,2,3,3,4,5]
assert bisect_left(nums, 3) == 2
assert bisect_right(nums, 3) == 4
assert bisect_left(nums, 2) == 1
assert bisect_right(nums, 2) == 2
assert bisect_left(nums, 6) == 6
assert bisect_right(nums, 6) == 6
