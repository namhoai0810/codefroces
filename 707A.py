colum,row = map(int, input().split())
flag = 0
for i in range(colum):
    for j in range(row):
        color = input()
        if(color == 'C' or color == 'M' or color == 'Y'):
            flag = 1
            break
    
if(flag == 1):
    print("#Color")
else:
    print("#Black&White")