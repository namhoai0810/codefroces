k, r = map(int, input().split())
check = True
h = 1
item = 0
while(check):
    item = item + 1
    h = k * item
    if(h % 10 == 0 or h % 10 == r): 
        check = False

print(item)