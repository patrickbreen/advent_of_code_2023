lines = [line.strip() for line in open("day12_input.txt", "r").readlines()]
# lines = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".split("\n")


# Idea: try to match the largest number (in as many combos as possible)

# then brute force search over the remaining combos.

# p1: ???.###
# p2: [1,1,3]
from functools import lru_cache

@lru_cache(maxsize=1000)
def combos(s, sizes, num_in_group=0):
    count = 0

    # success
    if not s:
        return not sizes and not num_in_group

    for c in [".", "#"] if s[0] == "?" else s[0]:


        # extend group
        if c == "#":
            count += combos(s[1:], sizes, num_in_group+1)

        # terminate group
        elif c == ".":
            # print("s:", s, "c:", c, "sizes:", sizes, "num_in_group:", num_in_group)
            # try to remove from sizes
            if num_in_group:
                if sizes and sizes[0] == num_in_group:
                    count += combos(s[1:], sizes[1:])
            # otherwise, just reset group
            else:
                count += combos(s[1:], sizes)



    # print("count:", count)
    return count


ps = [line.split() for line in lines]

# PART 1
print("part 1:", sum([combos(p1+".", tuple([int(n) for n in p2.split(",")])) for p1, p2 in ps]))

# PART 2
# prewarm the cache with subproblems


print("part 2:", sum([combos("?".join([p1]*5)+".", tuple([int(n) for n in p2.split(",")]*5)) for p1, p2 in ps]))
