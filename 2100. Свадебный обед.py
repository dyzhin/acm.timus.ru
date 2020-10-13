# https://acm.timus.ru/problem.aspx?space=1&num=2100

n = int(input())
i = 0
a = []
total = 0
while i < n:
	a.append(input())
	i += 1

for z in a:
	y = z.split('+')
	total += len(y)

if total + 2  == 13:
	print(total * 100 + 300)
else:
	print(total * 100 + 200)