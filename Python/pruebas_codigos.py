def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    actal_sum = sum(nums)

    return total + actal_sum

nums = [1, 3, 2, 6, 4]
missing = find_missing_number(nums)
print(missing)