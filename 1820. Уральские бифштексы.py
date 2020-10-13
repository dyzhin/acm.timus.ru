# https://acm.timus.ru/problem.aspx?space=1&num=1820

a, b = input().split()
n = int(a)
k = int(b)
if n <= k:
	print(2)
else:
	p = n*2 // k
	r = n*2 % k
	if r != 0:
		r = 1
	print(p + r)