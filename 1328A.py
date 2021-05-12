line = int(input())

while(line > 0):
    a, b = map(int, input().split())
    if(a % b == 0):
        print('0')
    else:
        print(b - (a%b))
    line = line - 1 
