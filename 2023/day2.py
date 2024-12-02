lines = open("day2_input.txt", "r").readlines()
# lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")


# PART 1
# bag = dict(red=12, green=13, blue=14)
# s = 0

# for game in lines:
#     game_id = int(game.split(":")[0].split()[1])
#     draws = game.split(":")[1].strip().split(";")
#     possible = True
#     for draw in draws:
#         balls = draw.split(",")
#         for ball in balls:
#             num, color = ball.strip().split()
#             # print("num:", int(num), "color:", color, "bag[color]", bag[color], "bag[color]<int(num)", bag[color]<int(num))
#             if bag[color] < int(num):
#                 possible = False
#     print("game_id:", game_id, "draws:", draws, "possible:", possible)
#     if possible:
#         s += game_id
#         print("sum:", s)


# Part 2
from functools import reduce
s = 0

for game in lines:
    min_bag = dict(red=0, green=0, blue=0)
    game_id = int(game.split(":")[0].split()[1])
    draws = game.split(":")[1].strip().split(";")
    for draw in draws:
        balls = draw.split(",")
        for ball in balls:
            num, color = ball.strip().split()
            # print("num:", int(num), "color:", color, "bag[color]", bag[color], "bag[color]<int(num)", bag[color]<int(num))
            min_bag[color] = max(min_bag[color], int(num))

    power = reduce((lambda x, y: x * y), min_bag.values())
    # print("game_id:", game_id, "draws:", draws)
    s += power
    print("sum:", s)