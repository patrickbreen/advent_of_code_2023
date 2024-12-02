lines = open("day3_input.txt", "r").readlines()



# lines = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split("\n")




# PART 1
# def is_sym(c):
#     return not c.isdigit() and not c == '.'

# def is_close_to_symbol(line_i, j, i, lines):
#     is_close = False
#     # check line above if exists
#     if line_i - 1>= 0:
#         line = lines[line_i-1].strip()
#         for k in range(j-1, i+1):
#             if k >= 0 and k < len(line) and is_sym(line[k]):
#                 # print("found above")
#                 is_close = True

#     # check before and after in line if exists
#     line = lines[line_i].strip()
#     # print("line:", line, "j:", j, "i:", i)
#     for k in range(j-1, i+1):
#         if k >= 0 and k < len(line) and is_sym(line[k]):
#             # print("found in line")
#             is_close = True

#     # check line below if exists
#     if line_i + 1 < len(lines):
#         line = lines[line_i+1].strip()
#         for k in range(j-1, i+1):
#             if k >= 0 and k < len(line) and is_sym(line[k]):
#                 # print("found below")
#                 is_close = True


#     return is_close

# s = 0
# # find every number and see if it is close to a symbol
# for line_i, line in enumerate(lines):
#     line = line.strip()
#     nums = []
#     j=0
#     for i in range(len(line)):
#         # handle end of line
#         if i == len(line)-1 and i>j and line[i].isdigit():
#             num = int(line[j:i+1])
#             if is_close_to_symbol(line_i, j, i, lines):
#                 s += num
#                 nums.append(num)
#         # handle: found a symbol in middle of line
#         elif not line[i].isdigit():
#             if i>j:
#                 num = int(line[j:i])
#                 if is_close_to_symbol(line_i, j, i, lines):
#                     s += num
#                     nums.append(num)
#                 j = i+1
#             else:
#                 j = i+1
#     print("nums:", nums, "s:", s)


# PART 2
def is_star(c):
    return c == '*'

d = dict()

def is_close_to_gear(line_i, j, i, lines, num):
    is_close = False
    # check line above if exists
    if line_i - 1>= 0:
        line = lines[line_i-1].strip()
        for k in range(j-1, i+1):
            if k >= 0 and k < len(line) and is_star(line[k]):
                # print("found above")
                is_close = True
                coord = (line_i-1, k)
                if coord in d:
                    d[coord].append(num)
                else:
                    d[coord] = [num]

    # check before and after in line if exists
    line = lines[line_i].strip()
    # print("line:", line, "j:", j, "i:", i)
    for k in range(j-1, i+1):
        if k >= 0 and k < len(line) and is_star(line[k]):
            # print("found in line")
            is_close = True
            coord = (line_i, k)
            if coord in d:
                d[coord].append(num)
            else:
                d[coord] = [num]

    # check line below if exists
    if line_i + 1 < len(lines):
        line = lines[line_i+1].strip()
        for k in range(j-1, i+1):
            if k >= 0 and k < len(line) and is_star(line[k]):
                # print("found below")
                is_close = True
                coord = (line_i+1, k)
                if coord in d:
                    d[coord].append(num)
                else:
                    d[coord] = [num]


    return is_close


# find every number and see if it is close to a symbol
for line_i, line in enumerate(lines):
    line = line.strip()
    nums = []
    j=0
    for i in range(len(line)):
        # handle end of line
        if i == len(line)-1 and i>j and line[i].isdigit():
            num = int(line[j:i+1])
            if is_close_to_gear(line_i, j, i, lines, num):
                nums.append(num)
        # handle: found a symbol in middle of line
        elif not line[i].isdigit():
            if i>j:
                num = int(line[j:i])
                if is_close_to_gear(line_i, j, i, lines, num):
                    nums.append(num)
                j = i+1
            else:
                j = i+1
    print("nums:", nums)

print("d:", d)

s = 0
for k, v in d.items():
    if len(v) == 2:
        prod = v[0] * v[1]
        s += prod
        print("k:", k, "prod:", prod, "s:", s)