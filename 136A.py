pres = int(input())
x = list(map(int, input().split()))
y = []
z = []

for i in range(1, pres + 1):
    z.append(i)

for i in range(pres):
    m = z[i]
    for j in range(pres):
        if m == x[j]:
            y.append(j+1)
for i in range(pres):
    print(y[i], end=" ")
