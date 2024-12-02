# Part 1
lines = open("day2_input.txt", "r").readlines()

safe = 0

for l in lines:
    nums = [int(n) for n in l.strip().split(" ")] 

    diffs = [nums[start+1] - nums[start] for start in range(len(nums)-1)]

    all_increasing = all([x > 0 for x in diffs])
    all_decreasing = all([x < 0 for x in diffs])
    right_magnitude = all([1 <= abs(x) <= 3 for x in diffs])

    if (all_increasing or all_decreasing) and right_magnitude:
        safe += 1

print("Part1", safe)


# Part 2
safe = 0

def is_safe(nums):
    diffs = [nums[start+1] - nums[start] for start in range(len(nums)-1)]

    all_increasing = all([x > 0 for x in diffs])
    all_decreasing = all([x < 0 for x in diffs])
    right_magnitude = all([1 <= abs(x) <= 3 for x in diffs])

    return (all_increasing or all_decreasing) and right_magnitude

for l in lines:
    nums = [int(n) for n in l.strip().split(" ")] 

    if is_safe(nums):
        safe += 1
    else:
        for skip in range(len(nums)):
            s = [x for i, x in enumerate(nums) if i != skip]
            if is_safe(s):
                safe += 1
                break

print("Part2", safe)