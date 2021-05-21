n, k = map(int, input().split())
slution = 0
max_time = 240 - k
i = 0

while(max_time > 0):
    i = i + 5
    max_time = max_time - i
    check = max_time
    if((check) >= 0 and slution < n):
        slution = slution + 1
    
print(slution)