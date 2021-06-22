line = int(input())
mis = 0
chi = 0
for i in range(line):
    mishka, chirs = map(int, input().split())
    if(mishka > chirs):
        mis = mis + 1
    elif(mishka < chirs):
        chi = chi + 1
    else:
        pass
if(mis > chi):
    print("Mishka")
elif(chi > mis):
    print("Chris")
else:
    print("Friendship is magic!^^")