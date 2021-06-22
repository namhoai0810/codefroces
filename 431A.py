a, b, c, d = list(map(int, input().split()))
string = input()
sum = 0
for i in range(len(string)):
    if(string[i] == '1'):
        sum = sum + a
    elif(string[i] == '2'):
        sum = sum + b
    elif(string[i] == '3'):
        sum = sum + c
    elif(string[i] == '4'):
        sum = sum + d

print(sum)