# https://acm.timus.ru/problem.aspx?space=1&num=1785

trans = {4: 'few', 9: 'several', 19: 'pack', 49: 'lots', 99: 'horde', 249: 'throng', 499: 'swarm', 999: 'zounds', 2000: 'legion'}
word = int(input())

for i in trans:
	if word <= i:
		print(trans[i])
		break