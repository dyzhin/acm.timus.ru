# https://acm.timus.ru/problem.aspx?space=1&num=1409

a, b = input().split()
g = int(a)
l = int(b)
summ = g + l - 1
print(summ - g, summ - l)