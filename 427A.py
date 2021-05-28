n = int(input())
lst = list(map(int, input().split()))
polis = 0
untreated = 0
for item in lst:
    if(item > 0):
        polis = polis + 1
    else:
        if(polis < 1):
            untreated = untreated + 1
        else:
            polis = polis - 1

print(untreated)