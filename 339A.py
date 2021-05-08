math = input()
n1 = n2 = n3 = 0
for i in range(0, len(math), 2):
    if(math[i] == '1'):
        n1 = n1 + 1
    elif(math[i] == '2'):
        n2 = n2 + 1
    elif(math[i] == '3'):
        n3 = n3 + 1
print(('1+' *n1 +'2+'*n2 + '3+'*n3)[:-1])
