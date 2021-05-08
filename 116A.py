line = int(input())
max_pres = 0
now_pres = 0
for i in range(line):
    out_pres, in_pres = map(int,input().split())
    now_pres = now_pres + in_pres
    now_pres = now_pres - out_pres
    max_pres = max(max_pres, now_pres)
    # print(max_pres)
print(max_pres)