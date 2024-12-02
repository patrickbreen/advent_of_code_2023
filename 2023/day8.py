lines = open("day8_input.txt", "r").readlines()

# lines = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)""".split("\n")


# lines = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)""".split("\n")


# PART 1
# instructions = lines[0].strip()

# nodes = dict()
# for line in lines[2:]:

#     k = line[0:3]
#     l = line[7:10]
#     r = line[12:15]
#     nodes[k] = (l, r)

# cur = "AAA"
# n = 0
# i = 0
# while cur != "ZZZ":
#     instruction = instructions[i]
#     if instruction == "L":
#         cur = nodes[cur][0]
#     else:
#         cur = nodes[cur][1]
#     n += 1
#     i = (i+1) % len(instructions)

# print("number of steps:", n)



# PART 2
instructions = lines[0].strip()

nodes = dict()
for line in lines[2:]:

    k = line[0:3]
    l = line[7:10]
    r = line[12:15]
    nodes[k] = (l, r)

starting_points = [node for node in nodes.keys() if node[-1] == "A"]

steps_list = []

for starting_point in starting_points:
    cur = starting_point
    n = 0
    i = 0
    while cur[-1] != "Z":
        instruction = instructions[i]
        if instruction == "L":
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        n += 1
        i = (i+1) % len(instructions)

    print("number of steps:", n)
    steps_list.append(n)

# get least common multiple:
import math
from functools import reduce

# I'm running an old version of python with no math.lcm().........
def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

print("lcm:", lcm(steps_list))
