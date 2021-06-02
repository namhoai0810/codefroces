citizens = int(input())
burles = list(map(int, input().split()))
burles.sort()
sum = 0
if(len(burles) == 1):
    print(0)
else:
    for item in range(0, len(burles) - 1):
        sum = sum + burles[-1] - burles[item]
    print(sum)
    