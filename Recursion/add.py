#rucursive function that return sum of first n integers
from re import I
import time

cummulatives = []
seconds = time.time()
def _sum_n(n):
    if n == 0:
        return 0
    else:
        return n + _sum_n(n-1)

for i in range(1,10):
    cummulatives.append(_sum_n(i))

print(cummulatives, seconds)






