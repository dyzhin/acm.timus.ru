# https://acm.timus.ru/problem.aspx?space=1&num=1880

short_list = []
long_list = []
all = [0, 1, 2]
ans = 0


short_list.append(int(input()))
long_list.append(input())
short_list.append(int(input()))
long_list.append(input())
short_list.append(int(input()))
long_list.append(input())

min_item_index = short_list.index(min(short_list))

all.remove(min_item_index)
min_list = long_list[min_item_index].split()

for i in min_list:
    if (i in long_list[all[0]]) and (i in long_list[all[1]]):
        ans += 1

print(ans)