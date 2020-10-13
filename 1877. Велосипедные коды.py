# https://acm.timus.ru/problem.aspx?space=1&num=1877

a = int(input())
b = int(input())
if (a % 2 == 0) or (b % 2 != 0):
	print('yes')
else:
	print('no')