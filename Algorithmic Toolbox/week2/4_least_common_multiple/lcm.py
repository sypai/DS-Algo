# Python Program to find the L.C.M. of two input number


def find_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if(greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


a, b = [int(x) for x in input().split()]

print(find_lcm(a, b))



