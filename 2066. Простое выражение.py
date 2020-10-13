# https://acm.timus.ru/problem.aspx?space=1&num=2066

a = int(input())
b = int(input())
c = int(input())

if a-b*c <= a-b-c:
	print(a-b*c)
else:
	print(a-b-c)