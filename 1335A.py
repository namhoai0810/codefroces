n = int(input())
lst = []
for i in range(0, n):
    candies = int(input())
    lst.append(candies)

for i in range(0, len(lst)):
    if(lst[i] == 1 or lst[i] == 2):
        print("0")
    else:
        print(int((lst[i] - 1) / 2))