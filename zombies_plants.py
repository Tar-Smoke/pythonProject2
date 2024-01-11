# Second task Zombies against plants.
# Plants are list[0] and zombies are list[1] in value.
# Keys are  numbers of tests
war_list = [
    {1: [[2, 4, 6, 8], [1, 3, 5, 7]]},
    {2: [[2, 4], [1, 3, 5, 7]]},
    {3: [[2, 4, 0, 8], [1, 3, 5, 7]]},
    {4: [[1, 2, 1, 1], [2, 1, 1, 1]]},
]

# Comparison of the initial strength of the attack
def compare(l1: list, l2: list):
    r = False
    if sum(l1) >= sum(l2):
        r = True
    else:
        r = False
    return r
# Comparison of the number of survivors
def war(l1: list, l2: list):
    result = False
    min_len = 0
    if len(l1) <= len(l2):
        min_len = len(l1)
    else:
        min_len = len(l2)
    ld1 = list(l1)
    ld2 = list(l2)
    for i in range(0, min_len):
        if l1[i] > l2[i]:
            ld2.pop(0)
        elif l1[i] == l2[i]:
            ld1.pop(0)
            ld2.pop(0)
        else:
            ld1.pop(0)

    if len(ld1) > len(ld2):
        result = True
    elif len(ld1) < len(ld2):
        result = False
    else:
        result = compare(l1, l2)

    return result
