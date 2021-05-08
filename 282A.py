line = int(input())
tmp = 0
sum = 0
for i in range(line):
    statement = input()
    if(statement.count('++') == 1):
        sum = sum + 1
    elif(statement.count('--') == 1):
        sum = sum - 1
    else:
        pass
print(sum)
