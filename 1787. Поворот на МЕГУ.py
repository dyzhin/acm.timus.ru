# https://acm.timus.ru/problem.aspx?space=1&num=1787

k, n = input().split()
a = input().split()
ans = 0
for i in a:
	if int(i) > int(k):
		ans += int(i) - int(k)
	else:
		ans -= int(k) - int(i)
		if ans < 0:
			ans = 0
print(ans)