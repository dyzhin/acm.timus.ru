# https://acm.timus.ru/problem.aspx?space=1&num=1001

import sys
import math
s = sys.stdin.read().split()
for w in reversed(s):
    print(f'{math.sqrt(int(w)):.4f}')