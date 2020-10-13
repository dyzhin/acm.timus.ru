# https://acm.timus.ru/problem.aspx?space=1&num=1197

n = int(input())
i = 0
a = []
while i < n:
    a.append(input())
    i += 1

for z in a:
    l = r = t = b = 2
    char = int.from_bytes(z[0].encode('utf-8'), 'little') - 96

    if char == 1:
        l = 0
    elif char == 2:
        l = 1
    elif char == 7:
        r = 1
    elif char == 8:
        r = 0

    char = int(z[1])

    if char == 1:
        b = 0
    elif char == 2:
        b = 1
    elif char == 7:
        t = 1
    elif char == 8:
        t = 0

    #	print('Слева: ', l)
    #	print('Справа: ', r)
    #	print('Сверху: ', t)
    #	print('Снизу: ', b)

    summ = l + r + t + b

    if summ == 8:
        print(8)
    elif summ == 7:
        print(6)
    elif summ == 6:
        print(4)
    elif summ == 5:
        print(3)
    else:
        print(2)
