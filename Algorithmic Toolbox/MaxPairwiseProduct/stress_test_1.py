from max_pair_product_NAIVE import max_naive
from max_pair_product_FAST import max_fast
import random

while True:
    rand_num = random.randint(0, 100)
    print(rand_num)
    a = []
    for i in range(rand_num):
        a.append(random.randint(0, 100000))

    print(a)

    res1 = max_naive(a, rand_num)
    res2 = max_fast(a, rand_num)

    if res1 != res2:
        print("Wrong Answer : ", res1, res2)
        break

    else:
        print("OK! ")
