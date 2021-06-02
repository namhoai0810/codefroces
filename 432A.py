menber, k = map(int,(input().split()))
victory = list(map(int, input().split()))
count = 0
for i in range(menber):
    if(5 - victory[i] >= k):
        count =count + 1

print(int(count/3))