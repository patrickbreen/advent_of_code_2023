
lines = open("day1_input.txt", "r").readlines()

# lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split("\n")

numbers = [dict(one='1', two='2', six='6'),
           dict(four='4', five='5', nine='9'),
           dict(three='3',seven='7', eight='8')]

rev_numbers = [dict(eno='1', owt='2', xis='6'),
           dict(ruof='4', evif='5', enin='9'),
           dict(eerht='3',neves='7', thgie='8')]

s = 0
for l in lines:
    first = ''
    last = ''
    stop = False

    rev_l = l[::-1]

    # forward
    for i, c in enumerate(l):
        print("i:", i)
        if c.isdigit():
            first = c
            stop = True
        for j in [3,4,5]:
            if i + j <= len(l):
                possible = l[i:i+j]
                if possible in numbers[j-3]:
                    first = numbers[j-3][possible]
                    stop = True
        if stop:
            break

    # reverse
    stop = False
    for i in range(len(l)):
        if rev_l[i].isdigit():
            last = rev_l[i]
            stop = True
        for j in [3,4,5]:
            if i + j <= len(l) and rev_l[i:i+j] in rev_numbers[j-3]:
                last = rev_numbers[j-3][rev_l[i:i+j]]
                stop = True
        if stop:
            break


    value = int(first + last)
    s += value
    print("value:", value, "s:", s)
print(s)
