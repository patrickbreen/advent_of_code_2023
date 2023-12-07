lines = open("day7_input.txt", "r").readlines()

# lines = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".split("\n")



# PART 1:
# # get list of [(hand, bid)]
# hands = []
# for line in lines:
#     hand, bid = line.strip().split()
#     hands.append([hand, int(bid)])

# # print("hands:", hands)

# def word_count(s):
#     wc = dict()
#     for c in s:
#         if c in wc:
#             wc[c] += 1
#         else:
#             wc[c] = 1
#     return wc

# def primary_rank(string):
#     wc = word_count(string)
#     s = set(wc.values())
#     if 5 in s:
#         return 7
#     elif 4 in s:
#         return 6
#     elif 3 in s and 2 in s:
#         return 5
#     elif 3 in s:
#         return 4
#     elif len(wc.values()) == 3:
#         return 3
#     elif 2 in s:
#         return 2
#     else:
#         return 1

# def label_strength(s):
#     strength = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
#     return sum([strength[c] * 14**(4-i) for i, c in enumerate(s)])

# # sort by rank
# sorted_hands = hands
# def compare(item1, item2):
#     score1 = primary_rank(item1[0]) * 14**5 + label_strength(item1[0])
#     score2 = primary_rank(item2[0]) * 14**5 + label_strength(item2[0])
#     return score1 - score2


# # Calling
# import functools
# sorted_hands.sort(key=functools.cmp_to_key(compare))
# print("sorted_hands:", sorted_hands)

# print("primary_rank:")
# for hand in sorted_hands:
#     print("hand:", hand, "primary_rank:", primary_rank(hand[0]))

# total = 0
# for i, hand in enumerate(sorted_hands):
#     total += (i+1) * hand[1]

# print("total:", total)


# PART 2:
# get list of [(hand, bid)]
hands = []
for line in lines:
    hand, bid = line.strip().split()
    hands.append([hand, int(bid)])

# print("hands:", hands)

def word_count(s):
    wc = dict()
    for c in s:
        if c in wc:
            wc[c] += 1
        else:
            wc[c] = 1
    return wc

def primary_rank(string):
    s_without_js = "".join([c for c in string if c != 'J'])
    wc = word_count(s_without_js)
    s = set(wc.values())
    number_of_js = sum([c == 'J' for c in string])
    if 5 in s or number_of_js >= 4 or (4 in s and number_of_js == 1) or (3 in s and number_of_js == 2) or (2 in s and number_of_js == 3):
        return 7
    elif 4 in s or (3 in s and number_of_js == 1) or (2 in s and number_of_js == 2) or number_of_js == 3:
        return 6
    elif (3 in s and 2 in s) or (number_of_js == 1 and len(wc.values()) == 2):
        return 5
    elif 3 in s or number_of_js == 2 or (number_of_js==1 and 2 in s):
        return 4
    elif len(wc.values()) == 3:
        return 3
    elif 2 in s or number_of_js == 1:
        return 2
    else:
        return 1

def label_strength(s):
    strength = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':1, 'Q':12, 'K':13, 'A':14}
    return sum([strength[c] * 14**(4-i) for i, c in enumerate(s)])

# sort by rank
sorted_hands = hands
def compare(item1, item2):
    score1 = primary_rank(item1[0]) * 14**5 + label_strength(item1[0])
    score2 = primary_rank(item2[0]) * 14**5 + label_strength(item2[0])
    return score1 - score2


# Calling
import functools
sorted_hands.sort(key=functools.cmp_to_key(compare))
print("sorted_hands:", sorted_hands)

print("primary_rank:")
for hand in sorted_hands:
    print("hand:", hand, "primary_rank:", primary_rank(hand[0]))

total = 0
for i, hand in enumerate(sorted_hands):
    total += (i+1) * hand[1]

print("total:", total)
