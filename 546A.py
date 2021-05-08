k,n,w = map(int, input().split())
sum = 0
for i in range(1, (w + 1)):
    tmp = k * i
    sum = sum + tmp

if((sum - n) < 0):
    print(0)
else:
    print(sum - n)

