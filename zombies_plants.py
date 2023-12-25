
# this file about war between zombies and plants
def war(l1, l2):
    ar1 = len(l1)
    ar2 = len(l2)
    the_force = False
    n1 = ar1
    n2 = ar2
    if sum(l1) == sum(l2):
        the_force = True
    else:
        the_force = False
    if ar1 > ar2:
        for x in range(ar2):
            if l1[x] > l2[x]:
                n2 -= 1
            elif l1[x] < l2[x]:
                n1 -= 1
            else:
                n1 -= 1
                n2 -= 1
    else:
        for x in range(ar1):
            if l1[x] > l2[x]:
                n2 -= 1
            elif l1[x] < l2[x]:
                n1 -= 1
            else:
                n1 -= 1
                n2 -= 1
    if n1 > n2:
        print("Zombies von")
    elif n1 < n2:
        print("Plants von")
    else:
        if sum(l1) > sum(l2):
            print("Zombies von")
        elif sum(l1) < sum(l2):
            print("Plants von")
        else:
            print("No one won!")
    return the_force
