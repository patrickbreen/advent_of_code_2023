lines = open("day4_input.txt", "r").readlines()

# lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

# PART 1
# def calc_score(matching_numbers):
#     s = 0
#     if matching_numbers >= 1:
#         s = 2**(matching_numbers-1)
#     return s

# total = 0
# for line in lines:
#     card = line.strip().split(":")
#     winning_numbers_raw, my_numbers_raw = card[1].strip().split("|")
#     winning_numbers = winning_numbers_raw.strip().split()
#     my_numbers = my_numbers_raw.strip().split()
#     matching_numbers = sum([number in winning_numbers for number in my_numbers ])
#     score = calc_score(matching_numbers)
#     total += score
#     print("score:", score, "total:", total)


# PART 2
total = 0
stack = []
matching_numbers_dict = dict()
def process_line(line_i):
    if line_i in matching_numbers_dict:
        matching_numbers = matching_numbers_dict[line_i]
    else:
        line = lines[line_i].strip()
        card = line.strip().split(":")
        winning_numbers_raw, my_numbers_raw = card[1].strip().split("|")
        winning_numbers = winning_numbers_raw.strip().split()
        my_numbers = my_numbers_raw.strip().split()
        matching_numbers = sum([number in winning_numbers for number in my_numbers])
        matching_numbers_dict[line_i] = matching_numbers
    for i in range(line_i+1, line_i+1+matching_numbers):
        if i < len(lines):
            stack.append(i)

# first pass
for line_i in range(len(lines)):
    process_line(line_i)
    total += 1
    # print("first pass - ", "stack:", stack, "total:", total)

# process stack
while len(stack) > 0:
    line_i = stack.pop()
    process_line(line_i)
    total += 1
    # print("in stack - ", "stack:", stack, "total:", total)
print("total:", total)
