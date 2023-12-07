lines = open("day6_input.txt", "r").readlines()

# lines = """Time:      7  15   30
# Distance:  9  40  200""".split("\n")


# PART 1
# times = [int(elem) for elem in lines[0].strip().split(":")[1].split()]
# distances = [int(elem) for elem in lines[1].strip().split(":")[1].split()]


# print("times:", times)
# print("distances:", distances)

# prod = 1
# for i in range(len(times)):
#     time = times[i]
#     distance = distances[i]

#     count = 0
#     for j in range(time):
#         speed = j
#         remaining_time = time - speed
#         my_distance = speed * remaining_time
#         if my_distance > distance:
#             count += 1

#     prod *= count

# print("prod:", prod)


# PART 2

count = 0
for speed in range(54708275):
    remaining_time = 54708275 - speed
    my_distance = speed * remaining_time
    if my_distance > 239114212951253:
        count += 1
print("count:", count)
