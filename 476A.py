room = int(input())
sum = 0
for i in range(0, room):
    room_in, room_free = map(int, input().split())
    if((room_free - room_in) >= 2):
        sum = sum + 1
    
print (sum)