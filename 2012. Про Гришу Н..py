# https://acm.timus.ru/problem.aspx?space=1&num=2012

a = int(input())
after_first = 12 - a
if after_first * 45 > 4 * 60:
	print('NO')
else:
	print('YES')