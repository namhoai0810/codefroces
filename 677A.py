number, wight = map(int, input().split())
member_wight = [int(x) for x in input().split()]
sum = 0
# print(member_wight)
for i in range(0, number):
    if(member_wight[i] > wight):
        sum = sum + 2
    else:
        sum = sum + 1
print(sum)