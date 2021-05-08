menber, score = map(int, input().split())
menber_nextRound = map(int, input().split())
count = 0
tmp = 0
listmenber = list(menber_nextRound)
# print(listmenber[-1])
for i in listmenber:
    if (i > 0 and i >= listmenber[score-1]):
        count = count + 1
    
print(count)