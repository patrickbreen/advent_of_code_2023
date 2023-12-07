lines = open("day5_input.txt", "r").readlines()

# lines = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".split("\n")


# PART 1:
# # get seeds array
# seeds = [int(seed) for seed in lines[0].strip().split(":")[1].strip().split(" ")]
# print("seeds:", seeds)
# m = dict()
# maps = []
# # make each map (low, high) -> increment
# for line in lines[1:]:
#     line = line.strip()

#     if "map:" in line:
#         if len(m) != 0:
#             maps.append(m)
#             m = dict()
#     elif line == "":
#         pass
#     else:
#         dest_low, source_low, r = [int(val) for val in line.split()]
#         m[(source_low, source_low+r)] = dest_low - source_low

# maps.append(m)
# print("maps:", maps)

# min_loc = -1
# # for each seed, trace through each map and get lowest 'location'
# for seed in seeds:
#     val = seed
#     for m in maps:
#         out = val
#         for k, inc in m.items():
#             (l, h) = k
#             if l <= val < h:
#                 out = val + inc
#         print("m:", m, "val:", val, "out:", out)
#         val = out
#     location = val
#     if min_loc == -1:
#         min_loc = location
#     min_loc = min(min_loc, location)

# print("min_loc:", min_loc)



# Part 2:
# get seeds array
seeds = [int(seed) for seed in lines[0].strip().split(":")[1].strip().split(" ")]
print("seeds:", seeds)
m = dict()
maps = []
# make each map (low, high) -> increment
for line in lines[1:]:
    line = line.strip()

    if "map:" in line:
        if len(m) != 0:
            maps.append(m)
            m = dict()
    elif line == "":
        pass
    else:
        dest_low, source_low, r = [int(val) for val in line.split()]
        m[(source_low, source_low+r)] = dest_low - source_low

maps.append(m)
print("maps:", maps)

# def get_location_from_seed(seed):
#     val = seed
#     for m in maps:
#         out = val
#         for k, inc in m.items():
#             (l, h) = k
#             if l <= val < h:
#                 out = val + inc
#         # print("m:", m, "val:", val, "out:", out)
#         val = out
#     return val

seed_pairs = []
pair = []
for i, seed in enumerate(seeds):
    pair.append(seed)
    if (i+1) % 2 == 0:
        seed_pairs.append(pair)
        pair = []

print("seed_pairs:", seed_pairs)

seed_ranges = []
for pair in seed_pairs:
    low, r = pair
    seed_ranges.append([low, low+r])

print("seed_ranges:", seed_ranges)
# flatten the seed pairs with the maps
# seed_ranges => ... => location ranges

in_ranges = seed_ranges


"""
For each range in input, map it, and add back new bits into the input.

if it doesn't map on any map, identity map it to the output, and then stop trying to map it.

output = unmapped_ranges + mapped_ranges
"""

# for each map
for m in maps:

    # for each range in the input
    unmapped_ranges = []
    mapped_ranges = []
    while len(in_ranges) > 0:
        no_overlap = True
        l_in, h_in = in_ranges.pop()

        # go through each range in this mapping
        for k, inc in m.items():
            l_source, h_source = k
            # case 1 in range 'inside' source - only 1 range is output
            if l_source <= l_in and h_in <= h_source:
                mapped_ranges.append([l_in + inc, h_in + inc])
                no_overlap = False
            # case 2 in range 'outside' source - 3 ranges are output
            elif l_in < l_source and h_source < h_in:
                in_ranges.append([l_in, l_source-1]) # outside goes back to be matched against other mappings
                mapped_ranges.append([l_source + inc, h_source + inc])
                in_ranges.append([h_source+1, h_in]) # outside goes back to be matched against other mappings
                no_overlap = False
            # case 3 no overlap
            elif h_source <= l_in or h_in <= l_source:
                pass
            # case 4 in range overlaps below map range - 2 ranges are output
            elif l_in < l_source < h_in:
                # print("case 4")
                in_ranges.append([l_in, l_source-1]) # outside goes back to be matched against other mappings
                mapped_ranges.append([l_source + inc, h_in + inc])
                no_overlap = False
            # case 5 in range overlaps above map range - 2 ranges are output
            elif l_in < h_source <= h_in:
                # print("case 5")
                mapped_ranges.append([l_in+inc, h_source-1+inc]) # outside goes back to be matched against other mappings
                in_ranges.append([h_source, h_in])
                no_overlap = False
        if no_overlap:
            unmapped_ranges.append([l_in, h_in])

    print("in_ranges:", in_ranges, "map:", m, "mapped_ranges:", mapped_ranges, "unmapped_ranges:", unmapped_ranges)
    in_ranges = mapped_ranges + unmapped_ranges

print("last out_ranges:", in_ranges)
m = in_ranges[0][0]
for i, r in enumerate(in_ranges):
    m = min(m, r[0])
    # print("r:", r)
    if r[1] < r[0]:
        print("found bad value:", r, "i:", i)

print("min:", m)
print("len(in_ranges):", len(in_ranges))




# min_loc = -1
# # for each seed, trace through each map and get lowest 'location'
# for seed_pair in seed_pairs:
#     low, r = seed_pair
#     print("seed_pair:", seed_pair)
#     for seed in range(low, low+r):
#         location = get_location_from_seed(seed)
#         if min_loc == -1:
#             min_loc = location
#         min_loc = min(min_loc, location)

# print("min_loc:", min_loc)
