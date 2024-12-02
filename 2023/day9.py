lines = open("day9_input.txt", "r").readlines()

# lines = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".split("\n")

seqs = [[int(elem) for elem in line.strip().split(" ")] for line in lines]


# PART 1
# def extrapolate(seq):
#     stack = [seq]

#     # extend the stack
#     while not all([elem == 0 for elem in stack[-1]]):
#         diffs = []
#         vals = stack[-1]
#         prev = vals[0]
#         for val in vals[1:]:
#             diffs.append(val - prev)
#             prev = val
#         stack.append(diffs)

#     # print("stack:", stack)

#     # rollback the stack
#     diff = stack[-2][-1]
#     for vals in stack[-3::-1]:
#         # print("vals:", vals, "diff:", diff)
#         diff += vals[-1]

#     return diff


# total = 0
# for seq in seqs:
#     e = extrapolate(seq)
#     total += e
#     print("seq:", seq, "extrapolate:", e, "total:", total)


# PART 2
def extrapolate_back(seq):
    stack = [seq]

    # extend the stack
    while not all([elem == 0 for elem in stack[-1]]):
        diffs = []
        vals = stack[-1]
        prev = vals[0]
        for val in vals[1:]:
            diffs.append(val - prev)
            prev = val
        stack.append(diffs)

    # print("stack:", stack)

    # rollback the stack
    diff = stack[-2][0]
    for vals in stack[-3::-1]:
        # print("vals:", vals, "diff:", diff)
        diff = vals[0] - diff

    return diff


total = 0
for seq in seqs:
    e = extrapolate_back(seq)
    total += e
    print("seq:", seq, "extrapolate:", e, "total:", total)