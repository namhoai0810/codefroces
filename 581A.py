a,b = map(int, input().split())
print(min(a,b), end=' ')
x = int((max(a,b) - min(a,b))/2)
print(x)